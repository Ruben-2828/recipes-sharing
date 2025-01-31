from django.urls import path
from .views import RecipeListView, RecipeDetailView
from . import views

app_name = "recipes_app"
urlpatterns = [
    path("", RecipeListView.as_view(), name="index"),
    path("recipe/<int:pk>/", RecipeDetailView.as_view(), name="detail"),
    path("recipe/add/", views.add_recipe, name="add"),
    path("reicipe/<int:recipe_id>/delete", views.delete_recipe, name="delete"),
]