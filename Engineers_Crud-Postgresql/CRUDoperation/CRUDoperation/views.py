import imp
from pyexpat.errors import messages
from django.shortcuts import render
from CRUDoperation.models import engineers
from django.contrib import messages
from CRUDoperation.forms import Engforms


def showEng(request):
    showall=engineers.objects.all()
    return render(request, 'index.html',{"data": showall})

def insertEng(request):
    if request.method=="POST":
        if request.POST.get('name'):
            saveRecord = engineers()
            saveRecord.name = request.POST.get('name')
            saveRecord.save()
            messages.success(request,saveRecord.name + ' is saved successfully.')
            return render(request, 'insert.html',{})
        else:
            return render(request, 'insert.html',{})
    else:
        return render(request, 'insert.html',{})

def Editeng(request, id):
    editengobj = engineers.objects.get(id=id)
    return render(request, 'edit.html',{"engineers": editengobj})


def updateeng(request, id):
    Updateeng = engineers.objects.get(id = id)
    form=Engforms(request.POST, instance=Updateeng)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Updated Successfully...')
        return render(request, 'edit.html',{"engineers": Updateeng})


def deleng(request, id):
    delengineer = engineers.objects.get(id = id)
    delengineer.delete()
    showdata = engineers.objects.all()
    return render(request, "index.html", {"data":showdata})

