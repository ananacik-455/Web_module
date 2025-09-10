from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField() #models.PositiveSmallIntegerField()


    # age = models.IntegerField(validators=[models.MinValueValidator(1), MaxValueValidator(120)])


