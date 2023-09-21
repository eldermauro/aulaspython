from django.shortcuts import render

def index(request):
    context = {
        'curso': 'Programação',
        'outro': 'aluno'
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')