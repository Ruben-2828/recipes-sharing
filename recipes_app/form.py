from django.forms import ModelForm
from .models import Recipe, Ingredient
from datetime import timedelta


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "duration", "description"]
        labels = {
            "title": "Recipe Title",
            "duration": "Duration (minutes)",
            "description": "Description",
        }


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ["name", "quantity"]
        labels = {"name": "Ingredient", "quantity": "Quantity"}
