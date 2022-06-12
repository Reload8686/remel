from django.shortcuts import render
from aloha_app_pro.models import Project

def project_index(request):
    aloha_app_pro = Project.objects.all()
    context = {
        'aloha_app_pro': aloha_app_pro
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

# Create your views here.
