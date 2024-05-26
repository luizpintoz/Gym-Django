from django.contrib.auth.models import User
from django.db import models
# Create your models here.

class BodyPart(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=150)
    series = models.IntegerField()
    repetitions = models.IntegerField()
    charge = models.IntegerField()
    rest_time = models.IntegerField()
    body_part = models.ManyToManyField(BodyPart)

    def __str__(self):
        return self.name

class Training(models.Model):
    EXERCISES_TYPE = [
        ("M","Masculino"),
        ("F","Feminino")
    ]

    NIVEL = [
        ("Avançado","AVC"),
        ("Intermediário","INT"),
        ("Iniciante","INC")
    ]

    type = models.CharField(max_length=1, choices=EXERCISES_TYPE)
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=150)
    days = models.IntegerField()
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    cover = models.ImageField(upload_to="trainsheet/covers/%Y/%m/%d/")
    exercises = models.ManyToManyField(Exercise)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    nivel_type = models.CharField(max_length=13, choices=NIVEL)

    def __str__(self) -> str:
        return self.title
