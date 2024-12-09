from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Comment

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, 'projects/project_detail.html', {'project': project})

def add_comment(request, id):
    project = get_object_or_404(Project, id=id)
    if request.method == 'POST':
        name = request.POST['name']
        text = request.POST['text']
        Comment.objects.create(project=project, name=name, text=text)
        return redirect('project_detail', id=id)
    return redirect('project_list')

# Create your views here.
