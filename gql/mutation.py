import graphene
from . import resolvers

class Mutation(graphene.ObjectType):
    create_meal = resolvers.CreateMeal.Field()