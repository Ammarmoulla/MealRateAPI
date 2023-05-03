import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import Meal, Rating
from django.contrib.auth.models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "username")

class MealType(DjangoObjectType):
    class Meta:
        model = Meal
        fields = ("id", "title", "description")

class RatingType(DjangoObjectType):
    user = graphene.Field(UserType, id=graphene.Int())
    class Meta:
        model = Rating
        fields = ("id", "meal", "user", "stars") 

class Query(graphene.ObjectType):
    all_meals = graphene.List(MealType)
    meal_by_id = graphene.Field(MealType, id=graphene.Int())
    all_rating = graphene.List(RatingType)
    rating_by_meal = graphene.List(RatingType, meal=graphene.ID())


    def resolve_all_meals(root, info):
        return Meal.objects.all()
    
    def resolve_meal_by_id(root, info, id):
        return Meal.objects.get(id=id)
    
    def resolve_all_rating(root, info):
        return Rating.objects.all()
    
    def resolve_rating_by_meal(root, info, meal=None):
        user = info.context.user
        print(meal, user)
        if meal:
            return Rating.objects.filter(meal__id=meal)
        
class CreateMeal(graphene.Mutation):
    Meal = graphene.Field(MealType, id=graphene.Int())

    class Arguments:
        title = graphene.String(requird=True)
        description = graphene.String(requrid=True)

    @classmethod
    def mutate(cls, root, info, )

    


schema = graphene.Schema(query=Query)

