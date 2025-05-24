from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    duration = models.DurationField()
    description = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="recipes",
        null=True,
    )

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="ingredients"
    )
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} {self.quantity}"
