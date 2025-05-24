from typing import Any
from django.forms import formset_factory, inlineformset_factory
from django.utils import timezone
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView, DeleteView
from .form import IngredientForm, RecipeForm
from recipes_app.models import Ingredient, Recipe
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes/list.html"
    context_object_name = "latest_recipes_list"
    queryset = Recipe.objects.order_by("-pub_date")[:20]


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/detail.html"
    context_object_name = "recipe"


@login_required
def add_recipe(request):
    IngredientFormSet = formset_factory(IngredientForm, min_num=1, extra=2)
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

            return redirect("recipes_app:detail", recipe.id)

    return render(
        request,
        "recipes/add.html",
        {
            "recipe_form": recipe_form,
            "ingredient_formset": ingredient_formset,
        },
    )


@login_required
def update_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe_form = RecipeForm(
        request.POST or None,
        prefix="recipe",
        instance=recipe,
    )

    IngredientFormSet = inlineformset_factory(
        Recipe,
        Ingredient,
        fields=["name", "quantity"],
        extra=0,
        can_delete=True,
    )
    ingredient_formset = IngredientFormSet(
        request.POST or None,
        instance=recipe,
        prefix="ingredient",
    )

    if request.method == "POST":
        if recipe_form.is_valid() and ingredient_formset.is_valid():
            recipe_form.save()
            ingredient_formset.save()

            return redirect("recipes_app:detail", recipe.id)

    return render(
        request,
        "recipes/add.html",
        {
            "recipe_form": recipe_form,
            "ingredient_formset": ingredient_formset,
            "update": True,
        },
    )


class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = "recipes/delete.html"
    success_url = "/"
