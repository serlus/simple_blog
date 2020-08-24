from django.http import HttpResponse
# Tem a função básica de responder as requisoções q nós fazemos pelo navegador


def home(request):  # sempre receberá o request
    return HttpResponse('Olá Django')
