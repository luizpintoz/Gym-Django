from django.urls import path, include
from . import views

app_name = "trainer"

urlpatterns = [
    path('', views.home, name='home'),
    path('trainingsheet/<int:id>/', views.trainsheet, name='trainingsheet'),
    path('trainingsheet/exercise/', views.exercise, name='exercise')
]
