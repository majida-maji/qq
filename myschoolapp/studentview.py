from django.shortcuts import render, redirect

from myschoolapp.forms import noteform, complaintform
from myschoolapp.models import Syllabus, ExamTable, TimeTable, StudyMaterial, Mark, ExamResult, Note, Complaint


def ssyllabusview(request):
    data=Syllabus.objects.all()
    return render(request,'student/ssyllabusview.html',{'data':data})

def sexamtableview(request):
    data=ExamTable.objects.all()
    return render(request,'student/sexamtableview.html',{'data':data})

def stimetableview(request):
    data=TimeTable.objects.all()
    return render(request,'student/stimetableview.html',{'data':data})

def sstudymaterialview(request):
    data=StudyMaterial.objects.all()
    return render(request,'student/sstudymaterialview.html',{'data':data})

def smarkview(request):
    data=Mark.objects.all()
    return render(request,'student/smarkview.html',{'data':data})

def sexamresultview(request):
    data=ExamResult.objects.all()
    return render(request,'student/sexamresultview.html',{'data':data})

def addnote(request):
    form=noteform()
    if request.method=='POST':
        form=noteform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('noteview')
    return render(request,'student/addnote.html',{'form':form})

def noteview(request):
    data=Note.objects.all()
    return render(request,'student/noteview.html',{'data':data})

def upnote(request,id):
    a=Note.objects.get(id=id)
    form=noteform(instance=a)
    if request.method=='POST':
        form=noteform(request.POST,request.FILES,instance=a)
        if form.is_valid():
            form.save()
            return redirect('noteview')
    return render(request,'student/upnote.html',{'form':form})

def delenote(request,id):
    Note.objects.get(id=id).delete()
    return redirect('noteview')


def addcomplaint(request):
    form=complaintform()
    if request.method=='POST':
        form=complaintform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('complaintview')
    return render(request,'student/addcomplaint.html',{'form':form})

def complaintview(request):
    data=Complaint.objects.all()
    return render(request,'student/complaintview.html',{'data':data})

def upcomplaint(request,id):
    a=Complaint.objects.get(id=id)
    form=complaintform(instance=a)
    if request.method=='POST':
        form=complaintform(request.POST,instance=a)
        if form.is_valid():
            form.save()
            return redirect('complaintview')
    return render(request,'student/upcomplaint.html',{'form':form})

def delecomplaint(request,id):
    Complaint.objects.get(id=id).delete()
    return redirect('complaintview')