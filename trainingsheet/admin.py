from django.contrib import admin
from .models import Exercise, Training

# Register your models here.

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    ...

@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    ...