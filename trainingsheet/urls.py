from django.urls import path
from . import views

app_name = "trainer"

urlpatterns = [
    path('', views.home, name='home'),
    path('trainingsheet/<int:id>/', views.trainsheet, name='trainingsheet')
]
