from django.db import models
from django.core.validators import MaxValueValidator

# Class for Gender
class Gender(models.Model):
    gender = models.CharField(max_length=6)

    def __str__(self):
        return self.gender

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.PositiveIntegerField(validators=[MaxValueValidator(125, 'Age cannot be more than 125')], null=True)
    gender = models.ForeignKey('Gender', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.last_name
        