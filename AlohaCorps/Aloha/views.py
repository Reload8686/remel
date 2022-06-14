from django.shortcuts import render

def Aloha(request):
    return render(request, 'Aloha.html', {})
