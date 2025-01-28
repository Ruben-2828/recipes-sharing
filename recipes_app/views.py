from django.forms import formset_factory
from django.utils import timezone
from django.shortcuts import get_object_or_404, render, redirect
from .form import IngredientForm, RecipeForm
from recipes_app.models import Recipe


def index(request):
    latest_recipes_list = Recipe.objects.order_by("-pub_date")[:20]
    context = {"latest_recipes_list": latest_recipes_list}
    return render(request, "recipes/index.html", context)


def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, "recipes/detail.html", {"recipe": recipe})


def add_recipe(request):
    IngredientFormSet = formset_factory(IngredientForm, min_num=1, extra=0)
    recipe_form = RecipeForm(prefix="recipe")
    ingredient_formset = IngredientFormSet(prefix="ingredient")

    if request.method == "POST":
        recipe_form = RecipeForm(request.POST, prefix="recipe")
        ingredient_formset = IngredientFormSet(request.POST, prefix="ingredient")

        if recipe_form.is_valid() and ingredient_formset.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.pub_date = timezone.now()
            recipe.save()

            for form in ingredient_formset:
                ingredient = form.save(commit=False)
                ingredient.recipe = recipe
                ingredient.save()

            return redirect("recipes_app:index")

    return render(
        request,
        "recipes/add.html",
        {
            "recipe_form": recipe_form,
            "ingredient_formset": ingredient_formset,
        },
    )
