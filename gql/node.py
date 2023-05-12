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
