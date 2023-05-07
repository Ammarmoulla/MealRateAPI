from django.contrib import admin
from .models import Meal, Rating
# Register your models here.
class Mealadmin(admin.ModelAdmin):
    list_display = ["id", "title", "description"]
    list_filter = ["title", "description"]
    search_fields = ["title", "description"]

class Ratingadmin(admin.ModelAdmin):
    list_filter = ["meal", "user"]
    search_fields = ["meal"]

admin.site.register(Meal, Mealadmin)
admin.site.register(Rating, Ratingadmin)