from graphene import relay, ObjectType
from graphene_django.filter import DjangoFilterConnectionField
from gql import node

class Query(ObjectType):
    user = relay.Node.Field(node.UserNode)
    users = DjangoFilterConnectionField(node.UserNode)
    
    meal = relay.Node.Field(node.MealNode)
    meals = DjangoFilterConnectionField(node.MealNode)
    
    rating = relay.Node.Field(node.RatingNode)
    ratings = DjangoFilterConnectionField(node.RatingNode)


    