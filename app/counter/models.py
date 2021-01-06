from django.db import models

class CalorieCount(models.Model):
    Food = models.CharField(max_length=200)
    Carbohydrates = models.IntegerField()
    Calories = models.IntegerField()

    def __str__(self):
        return self.Food





# Create your models here.
