from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from myschoolapp.forms import noteform, complaintform, projectform, assignmentform, seminarform, hwform, schatform, \
    onlinepaymentform
from myschoolapp.models import Syllabus, ExamTable, TimeTable, StudyMaterial, Mark, ExamResult, Note, Complaint, \
    Project, Assignment, Seminar, Hw, CommunityGroup, StudentLogin, StudentAppointment, Schat, Notification, \
    OnlinePayment

@login_required(login_url='loginpage')
def ssyllabusview(request):
    data=Syllabus.objects.all()
    return render(request,'student/ssyllabusview.html',{'data':data})
@login_required(login_url='loginpage')
def sexamtableview(request):
    data=ExamTable.objects.all()
    return render(request,'student/sexamtableview.html',{'data':data})
@login_required(login_url='loginpage')
def stimetableview(request):
    data=TimeTable.objects.all()
    return render(request,'student/stimetableview.html',{'data':data})
@login_required(login_url='loginpage')
def sstudymaterialview(request):
    data=StudyMaterial.objects.all()
    return render(request,'student/sstudymaterialview.html',{'data':data})
@login_required(login_url='loginpage')
def smarkview(request):
    data=Mark.objects.all()
    return render(request,'student/smarkview.html',{'data':data})
@login_required(login_url='loginpage')
def sexamresultview(request):
    data=ExamResult.objects.all()
    return render(request,'student/sexamresultview.html',{'data':data})
@login_required(login_url='loginpage')
def addnote(request):
    form=noteform()
    if request.method=='POST':
        form=noteform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('noteview')
    return render(request,'student/addnote.html',{'form':form})
@login_required(login_url='loginpage')
def noteview(request):
    data=Note.objects.all()
    return render(request,'student/noteview.html',{'data':data})
@login_required(login_url='loginpage')
def upnote(request,id):
    a=Note.objects.get(id=id)
    form=noteform(instance=a)
    if request.method=='POST':
        form=noteform(request.POST,request.FILES,instance=a)
        if form.is_valid():
            form.save()
            return redirect('noteview')
    return render(request,'student/upnote.html',{'form':form})
@login_required(login_url='loginpage')
def delenote(request,id):
    Note.objects.get(id=id).delete()
    return redirect('noteview')

@login_required(login_url='loginpage')
def addcomplaint(request):
    form=complaintform()
    u=request.user
    if request.method=='POST':
        form=complaintform(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
            return redirect('complaintview')
    return render(request,'student/addcomplaint.html',{'form':form})
@login_required(login_url='loginpage')
def complaintview(request):
    data=Complaint.objects.filter(user=request.user)
    return render(request,'student/complaintview.html',{'data':data})
@login_required(login_url='loginpage')
def upcomplaint(request,id):
    a=Complaint.objects.get(id=id)
    form=complaintform(instance=a)
    if request.method=='POST':
        form=complaintform(request.POST,instance=a)
        if form.is_valid():
            form.save()
            return redirect('complaintview')
    return render(request,'student/upcomplaint.html',{'form':form})
@login_required(login_url='loginpage')
def delecomplaint(request,id):
    Complaint.objects.get(id=id).delete()
    return redirect('complaintview')
@login_required(login_url='loginpage')
def addproject(request):
    form=projectform()
    u=request.user
    if request.method=='POST':
        form=projectform(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
            return redirect('projectview')
    return render(request,'student/addproject.html',{'form':form})
@login_required(login_url='loginpage')
def projectview(request):
    data=Project.objects.filter(user=request.user)
    return render(request,'student/projectview.html',{'data':data})
@login_required(login_url='loginpage')
def upproject(request,id):
    a=Project.objects.get(id=id)
    form=projectform(instance=a)
    if request.method=='POST':
        form=projectform(request.POST,request.FILES,instance=a)
        if form.is_valid():
            form.save()
            return redirect('projectview')
    return render(request,'student/upproject.html',{'form':form})
@login_required(login_url='loginpage')
def deleproject(request,id):
    Project.objects.get(id=id).delete()
    return redirect('projectview')


@login_required(login_url='loginpage')
def addassignment(request):
    form=assignmentform()
    u=request.user
    if request.method=='POST':
        form=assignmentform(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
            return redirect('assignmentview')
    return render(request,'student/addassignment.html',{'form':form})
@login_required(login_url='loginpage')
def assignmentview(request):
    data=Assignment.objects.filter(user=request.user)
    return render(request,'student/assignmentview.html',{'data':data})
@login_required(login_url='loginpage')
def upassignment(request,id):
    a=Assignment.objects.get(id=id)
    form=assignmentform(instance=a)
    if request.method=='POST':
        form=assignmentform(request.POST,request.FILES,instance=a)
        if form.is_valid():
            form.save()
            return redirect('assignmentview')
    return render(request,'student/upassignment.html',{'form':form})
@login_required(login_url='loginpage')
def deleassignment(request,id):
    Assignment.objects.get(id=id).delete()
    return redirect('assignmentview')

@login_required(login_url='loginpage')
def addseminar(request):
    form=seminarform()
    u=request.user
    if request.method=='POST':
        form=seminarform(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()

            return redirect('seminarview')
    return render(request,'student/addseminar.html',{'form':form})
@login_required(login_url='loginpage')
def seminarview(request):
    data=Seminar.objects.filter(user=request.user)
    return render(request,'student/seminarview.html',{'data':data})
@login_required(login_url='loginpage')
def upseminar(request,id):
    a=Seminar.objects.get(id=id)
    form=seminarform(instance=a)
    if request.method=='POST':
        form=seminarform(request.POST,request.FILES,instance=a)
        if form.is_valid():
            form.save()
            return redirect('seminarview')
    return render(request,'student/upseminar.html',{'form':form})
@login_required(login_url='loginpage')
def deleseminar(request,id):
    Seminar.objects.get(id=id).delete()
    return redirect('seminarview')
@login_required(login_url='loginpage')
def addhw(request):
    form=hwform()
    u=request.user
    if request.method=='POST':
        form=hwform(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
            return redirect('hwview')
    return render(request,'student/addhw.html',{'form':form})
@login_required(login_url='loginpage')
def hwview(request):
    data=Hw.objects.filter(user=request.user)
    return render(request,'student/hwview.html',{'data':data})
@login_required(login_url='loginpage')
def uphw(request,id):
    a=Hw.objects.get(id=id)
    form=hwform(instance=a)
    if request.method=='POST':
        form=hwform(request.POST,request.FILES,instance=a)
        if form.is_valid():
            form.save()
            return redirect('hwview')
    return render(request,'student/uphw.html',{'form':form})
@login_required(login_url='loginpage')
def delehw(request,id):
    Hw.objects.get(id=id).delete()
    return redirect('hwview')
@login_required(login_url='loginpage')
def scommunitygroupview(request):
    data=CommunityGroup.objects.all()
    return render(request,'student/scommunitygroupview.html',{'data':data})

@login_required(login_url='loginpage')
def sjoin_community(request, id):
    s = CommunityGroup.objects.get(id=id)
    c = StudentLogin.objects.get(user=request.user)
    print(c)
    appointment = StudentAppointment.objects.filter(user=c, schedule=s)
    if appointment.exists():
        messages.info(request, 'You Have Already Requested Appointment for this Schedule')
        return redirect('scommunitygroupview')
    else:
        if request.method == 'POST':
            obj = StudentAppointment()
            obj.user = c
            obj.schedule = s
            obj.save()
            messages.info(request, 'Appointment Booked Successfully')
            return redirect('sappointment_view')
    return render(request, 'student/take_sappointment.html', {'schedule': s})


@login_required(login_url='loginpage')
def sappointment_view(request):
    c = StudentLogin.objects.get(user=request.user)
    a = StudentAppointment.objects.filter(user=c)
    return render(request, 'student/sappointment_view.html', {'appointment': a})






@login_required(login_url='loginpage')
def addschat(request):
    form=schatform()
    u=request.user
    if request.method=='POST':
        form=schatform(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
            return redirect('schatview')
    return render(request,'student/addschat.html',{'form':form})
@login_required(login_url='loginpage')
def schatview(request):
    # u=Schat.objects.get(user=request.user)
    # print(u)
    data=Schat.objects.all()
    return render(request,'student/schatview.html',{'data':data})

@login_required(login_url='loginpage')
def snotificationview(request):
    u=StudentLogin.objects.get(user=request.user)
    data=Notification.objects.filter(name_and_email=u)
    return render(request,'student/snotificationview.html',{'data':data})
@login_required(login_url='loginpage')
def spay_bill(request,id):
    bi=Notification.objects.get(id=id)
    form=onlinepaymentform()
    u = request.user
    if request.method =='POST':
        card=request.POST.get('card_no')
        c=request.POST.get('cvv')
        da=request.POST.get('exp_date')
        OnlinePayment(card_no=card,cvv=c,exp_date=da,amount=bi).save()
        bi.status=1
        bi.save()
        messages.info(request,'bill paid successfully')
        return redirect('snotificationview')
    return render(request,'student/spaybill.html')
@login_required(login_url='loginpage')
def spay_in_direct(request, id):
    bi = Notification.objects.get(id=id)
    bi.status = 2
    bi.save()
    messages.info(request, 'Choosed to Pay Fee Direct in office')
    return redirect('snotificationview')
@login_required(login_url='loginpage')
def spay_history_view(request):
    data=Notification.objects.all()
    return render(request,'student/spayment_history_view.html',{'data':data})


