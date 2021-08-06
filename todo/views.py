from django.forms.forms import Form
from django.shortcuts import render,redirect
from .models import *
from .forms import FormTarea


def home(req):
    data=Tarea.objects.all()
    context={'tareas':data}
    return render(req,'todo/index.html',context)

def addTarea(req):
    if req.method=='POST':
        form=FormTarea(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        context={'form':FormTarea}
        return render(req,'todo/insert.html',context)

def delete(req,id_tarea):
    if id_tarea==None:
        return redirect('home')
    tarea=Tarea.objects.get(id=id_tarea)
    tarea.delete()
    return redirect('home')

def update(req,id_tarea):
    if id_tarea!=None:
        tarea=Tarea.objects.get(id=id_tarea)
        if tarea!=None:
            if req.method=='POST':
                form=FormTarea(req.POST,instance=tarea)
                if form.is_valid():
                    form.save()
                    return redirect('home')
            else:
                context={'form':FormTarea(instance=tarea)}
                return render(req,'todo/update.html',context)
        else:
            print('no hay un dato con ese id')
            return redirect('home')
    
    else:
        return redirect('home')

