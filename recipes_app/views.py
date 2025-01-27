from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from recipes_app.models import Recipe


def index(request):
    latest_recipes_list = Recipe.objects.order_by("-pub_date")[:5]
    context = {"latest_recipes_list": latest_recipes_list}
    return render(request, "recipes/index.html", context)

def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, "recipes/detail.html", {"recipe": recipe})

def add_recipe(request):
    return render(request, "recipes/add.html")