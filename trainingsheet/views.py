from django.shortcuts import render
from .models import Training
# Create your views here.

def home(request):
    training = Training.objects.all().order_by('-id')

    return render(request, "trainingsheet/pages/home.html", context={
        'trainer':training,
    })


def trainsheet(request, id):
    training = Training.objects.get(id=id)
    exercise = training.exercises.all()
    list_body = []
    bodys = []

    '''
    Isso foi necessário pq estava repetindo o nome da parte do 
    corpo mais de uma vez se tivesse mais de 
    um exercício para o mesmo grupo muscular
    '''
    for exe in exercise:
        #pega a parte do corpo do exercicio
        part = exe.body_part.all()
        print(part)

        for body in part:#navega na QuerySet que é gerada quando busca todos os dados de uma objeto
            print(type(body))
            if body.name in list_body:#Verifica se o nome da parte do corpo já está na lista
                pass
            else:
                list_body.append(body.name)#Se não estiver ele adiciona
                bodys.append(body)                
    
    return render(request, 'trainingsheet/pages/training.html', context={
        "train":training,
        "is_detail_page":True,
        "exercises": exercise,
        "body_parts":bodys,
        "list_body":list_body,
    })

def exercise(request):
    training = Training.objects.all().order_by('-id')
    return render(request, "trainingsheet/pages/home.html", context={
        'trainer':training
    })