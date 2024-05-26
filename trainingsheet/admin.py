from django.contrib import admin
from .models import Exercise, Training, BodyPart

# Register your models here.

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    ...

@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    ...

@admin.register(BodyPart)
class BodyPartAdmin(admin.ModelAdmin):
    ...