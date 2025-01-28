from django.urls import path

from . import views

app_name = "recipes_app"
urlpatterns = [
    path("", views.index, name="index"),
    path("recipe/<int:recipe_id>/", views.detail, name="detail"),
    path("add/", views.add_recipe, name="add"),
    path("delete/<int:recipe_id>/", views.delete_recipe, name="delete"),
]