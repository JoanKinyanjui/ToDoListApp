from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Tasks
from django.urls import reverse

def index(request):
    task=Tasks.objects.all().values()
    context={
        'task': task
    }
    return render(request,'index.html',context)


    
def addnew(request):
    x = request.POST['newtask']
    task = Tasks(task=x)
    task.save()
    return HttpResponseRedirect(reverse('index'))



def edit(request,id):
     task=Tasks.objects.get(id=id)
     context={
         'task':task
     }
     return render(request,'edit.html',context)

def update(request,id):
    newtask = request.POST['updatedtask']
    spectask=Tasks.objects.get(id=id)
    spectask.task = newtask
    spectask.save()
    return HttpResponseRedirect(reverse('index'))



def delete(request,id):
    task=Tasks.objects.get(id=id)
    task.delete()
    return HttpResponseRedirect(reverse('index'))