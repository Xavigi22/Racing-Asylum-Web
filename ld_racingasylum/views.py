from django.shortcuts import render

def hola_mundo(request):
	return render(request, 'ld_racingasylum/index.html')

def inicio(request):
    return render(request, 'ld_racingasylum/index2.html')
