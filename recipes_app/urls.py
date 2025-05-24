from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeDeleteView
from . import views

app_name = "recipes_app"
urlpatterns = [
    path("", RecipeListView.as_view(), name="index"),
    path("recipe/<int:pk>/", RecipeDetailView.as_view(), name="detail"),
    path("recipe/add/", views.add_recipe, name="add"),
    path("recipe/<int:recipe_id>/update/", views.update_recipe, name="update"),
    path("recipe/<int:pk>/delete", RecipeDeleteView.as_view(), name="delete"),
]