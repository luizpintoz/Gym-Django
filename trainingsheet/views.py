from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from utils.trainingsheet.factory import make_recipe
from random import randint

# Create your views here.

def home(request):
    return render(request, "trainingsheet/pages/home.html", context={
        'trainer':[make_recipe() for _ in range(10)]
    })

def trainsheet(request, id):
    body = ["Chest", "Back", "Arms", "Shoulders", "Legs"]

    return render(request, 'trainingsheet/pages/training.html', context={
        "train":make_recipe(),
        "is_detail_page":True,
        "bfor":[x for x in range(randint(1,6))],
        "get":body
    })