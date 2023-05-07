from django.shortcuts import render, get_object_or_404
from .models import Meal, Rating
from .serializers import MealSerializer, RatingSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

class MealViewset(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    @action(methods=['post'], detail=True)
    def meal_rate(self, request, pk=None):
        pass


class RatingViewset(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer