from base64 import standard_b64decode
from graphene import relay
from graphene_django import DjangoObjectType
from django.contrib.auth.models import User
from api.models import Meal, Rating

class UserNode(DjangoObjectType):
    class Meta:
        model = User
        exclude_fields = ['password']
        filter_fields = {
            'email': ['exact'],
            'username': ['exact'],
        }
        interfaces = (relay.Node, )

class MealNode(DjangoObjectType):
    class Meta:
        model = Meal
        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith'],
            'description': ['exact', 'icontains'],
        }
        interfaces = (relay.Node, )

class RatingNode(DjangoObjectType):
    class Meta:
        model = Rating
        filter_fields = {
            'meal': ['exact'],
            'user': ['exact'],
            'stars': ['exact'],
            'meal__title': ['exact', 'icontains'],
        }
        interfaces = (relay.Node, )


def get_node_id(id_base64, node):
    _type, _id = standard_b64decode(id_base64.encode('utf-8')).decode('utf-8').split(':')
    assert _type == node._meta.name
    return _id