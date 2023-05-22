import graphene
from django.db import transaction
from django.contrib.auth.models import User
from . import node
from api import models

class CreateMeal(graphene.relay.ClientIDMutation):
    class Input:
        title = graphene.NonNull(graphene.String)
        description = graphene.NonNull(graphene.String)

    meal = graphene.Field(node.MealNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        
        transaction.set_autocommit(False)
        meal = None

        try:
            meal = models.Meal(
                title = input.get("title"),
                description = input.get("description"),
                )
            meal.save()
            meal.commit()
        except:
            transaction.rollback()
        
        return CreateMeal(meal=meal)
    
# mutation{
#   createMeal(input: { title: "souq", description: "souq" }) {
#     meal {
#       id
#       title
#       description
#     }
#   }
# }
