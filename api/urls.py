from django.contrib import admin
from django.urls import path, include
from .views import MealViewset, RatingViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('meals', MealViewset)
router.register('ratings', RatingViewset)
urlpatterns = [
    path('', include(router.urls)),
]
