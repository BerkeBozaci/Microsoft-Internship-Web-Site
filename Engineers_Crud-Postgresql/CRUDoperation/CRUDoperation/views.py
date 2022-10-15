import imp
import re
from turtle import isvisible
from multiprocessing import context
from pyexpat.errors import messages
from django.shortcuts import render
from CRUDoperation.models import *
from django.shortcuts import redirect, render
from django.contrib import messages
from CRUDoperation.forms import *
from CRUDoperation.models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect
import CRUDoperation
from CRUDoperation.models import EngineerLearningPaths, Engineers, Learningpaths, Learningpathsteps, Mips

# Create your views here.

def index(request):
    return render(request, 'index.html')

def adminView(request):
    if 'Engineer Name' in request.POST:
        engineer = Engineers(name=request.POST['Engineer Name'])
        engineer.save()
    if 'Engineer Delete' in request.POST:
        engineer = Engineers.objects.get(engineer_id=request.POST['Engineer Delete'])
        engineer.delete()
    if 'Path Name' in request.POST:
        path = Learningpaths(description=request.POST['Path Name'], mip=Mips.objects.get(mip_id=request.POST['PathMip ID']))
        path.save()
    if 'Step Name' in request.POST:
        step = Learningpathsteps(name = request.POST['Step Name'], learningpath=Learningpaths.objects.get(learningpath_id=request.POST['Path ID']))
        step.save()
    if 'Mip Name' in request.POST:
        mip = Mips(mip_name=request.POST['Mip Name'])
        mip.save()
    engineers = Engineers.objects.all()
    return render(request, 'cadmin.html', {'engineers':engineers})

def Editeng(request, engineer_id):
    editengobj = Engineers.objects.get(engineer_id=engineer_id)
    return render(request, 'edit.html',{"engineers": editengobj})

def updateeng(request, engineer_id):
    Updateeng = Engineers.objects.get(engineer_id = engineer_id)
    form=Engforms(request.POST, instance=Updateeng)
    if form.is_valid():
        form.save()
        return render(request, 'edit.html',{"engineers": Updateeng})
    else:
        return render(request, 'edit.html',{"engineers": Updateeng})


def mipView(request, pk):
    currEng = Engineers.objects.get(engineer_id = pk)
    context = {"data":currEng}
    messages.success(request,'Engineer Id: ' + str(currEng.engineer_id) + ' Engineer Name: ' + currEng.name)
    engLPs = EngineerLearningPaths.objects.filter(engineer_id=pk)
    context = {"data":currEng, 'engLPs':engLPs}
    return render(request, 'mips.html' ,context)

def stepView(request, pk, lpk):
    lpsteps = Learningpathsteps.objects.filter(learningpath_id=lpk)
    return render(request, 'steps.html', {'lpsteps':lpsteps})

def mipList(request):

    if 'Mip Delete' in request.POST:
        EngineerLearningPaths.objects.filter(learningpath__mip__mip_id=request.POST['Mip Delete']).delete()
        Learningpaths.objects.filter(mip_id=request.POST['Mip Delete']).delete()
        mip = Mips.objects.get(mip_id=request.POST['Mip Delete'])
        mip.delete()
        mip_list = Mips.objects.all()
        return render(request, 'miplist.html', {'mip_list':mip_list})  
    else:
        mip_list = Mips.objects.all()
        return render(request, 'miplist.html', {'mip_list':mip_list})

def pathList(request):
    if 'Lp Delete' in request.POST:
        EngineerLearningPaths.objects.filter(learningpath_id=request.POST['Lp Delete']).delete()
        learningpath = Learningpaths.objects.get(learningpath_id=request.POST['Lp Delete'])
        learningpath.delete()
        path_list = Learningpaths.objects.all()
        return render(request, 'lplist.html', {'path_list':path_list})
    else:
        path_list = Learningpaths.objects.all()
        return render(request, 'lplist.html', {'path_list':path_list})

def stepList(request):
    if 'Step Delete' in request.POST:
        EngineerLearningPathSteps.objects.filter(learningpath_id=request.POST['Step Delete']).delete()
        learnigpathstep = Learningpathsteps.objects.get(lp_step_id=request.POST['Step Delete'])
        learnigpathstep.delete()
        step_list = Learningpathsteps.objects.all()
        return render(request, 'steplist.html', {'step_list':step_list})
    else:
        step_list = Learningpathsteps.objects.all()
        return render(request, 'steplist.html', {'step_list':step_list})

def delMip(request, pk): 
    currMip = Mips.objects.get(mip_id = pk)
    if request.method == "POST":
        currMip.delete()
        return redirect('/')    #silince aynı sayfada kalamaz home a döner
    context = {'item':currMip}
    return render(request,'delMip.html',context)

def delPath(request, pk):
    curEngPath = Learningpaths.objects.get(learningpath_id = pk)
    if request.method == "POST":
        curEngPath.delete()
        return redirect('/')
    context = {'item': curEngPath}
    return render(request, 'delPath.html', context)

def delStep(request, pk):
    curEngPathStep = Learningpathsteps.objects.get(lp_step_id = pk)
    if request.method == "POST":
        curEngPathStep.delete()
        return redirect('/')
    context = {'item': curEngPathStep}
    return render(request, 'delStep.html', context)

def createEngLearningPath(request, pk):
    currEng = Engineers.objects.get(engineer_id = pk)
    form = EngLPForms(initial={'engineer': currEng})
    if request.method == "POST":
        form = EngLPForms(request.POST)
        if form.is_valid:
            form.save()
            return redirect(request.META.get('HTTP_REFERER'))
    context = {'form': form}

    return render(request, 'engLP.html', context)

# def updateEngLP(request,pk):
#     currLP = EngineerLearningPaths.objects.get(englp_id = pk)  #ne yapıyosan onun idsini almalısın eng falan değil
#     form = EngLPForms(instance=currLP)
#     if request.method == "POST":
#         form = EngLPForms(request.POST,instance=currLP)
#         if form.is_valid:
#             form.save()
#             return redirect('/')
#     context = {'form':form, 'lp':currLP}
#     return render(request, 'engLP.html',context)


# def deleteEngLP(request,pk):
#     currLP = EngineerLearningPaths.objects.get(englp_id = pk)  
#     if request.method == "POST":
#         currLP.delete()
#         return redirect('/')    #silince aynı sayfada kalamaz home a döner
#     context = {'item':currLP}
#     return render(request,'deleteEngLP.html',context)

def createEngineerLearningPathStep(request,pk):
    currEng = Engineers.objects.get(engineer_id = pk)
    form = EngLPStepForms(initial={'engineer':currEng})
    if request.method == "POST":
        form = EngLPStepForms(request.POST)
        if form.is_valid:
            form.save()
            return redirect(request.META.get('HTTP_REFERER'))
    context = {'form':form}
    return render(request, 'engLPStep.html',context)

# def updateEngLPStep(request,pk):
#     currLP = EngineerLearningPaths.objects.get(englpstep_id = pk)  #ne yapıyosan onun idsini almalısın eng falan değil
#     form = EngLPStepForms(instance=currLP)
#     if request.method == "POST":
#         form = EngLPStepForms(request.POST,instance=currLP)
#         if form.is_valid:
#             form.save()
#             return redirect('/')
#     context = {'form':form}
#     return render(request, 'engLPStep.html',context)

# def deleteEngLPStep(request,pk):
#     currLP = EngineerLearningPathSteps.objects.get(englpstep_id = pk)  
#     if request.method == "POST":
#         currLP.delete()
#         return redirect('/')    
#     context = {'item':currLP}
#     return render(request,'deleteEngLPStep.html',context)




