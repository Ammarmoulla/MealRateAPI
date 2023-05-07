from rest_framework import serializers
from .models import Meal, Rating
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ("id", "title", "description", "rating")


class RatingSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Rating
        fields = ("id", "meal", "user", "stars") 
