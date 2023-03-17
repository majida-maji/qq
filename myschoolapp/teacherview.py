from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from myschoolapp.forms import teacherattendanceform, communitygroupform, studymaterial, markform, seminarform, \
    schatform, pchatform, notificationform
from myschoolapp.models import StudentLogin, ParentLogin, StaffMeeting, Duty, TeacherAttendance, TeacherLogin, \
    CommunityGroup, Syllabus, ExamTable, TimeTable, ParentsMeeting, StudyMaterial, Mark, ExamResult, Project, \
    Assignment, Seminar, Hw, Appointment, StudentAppointment, ParentAppointment, ParentComplaint, Complaint, Schat, \
    Pchat, Notification

@login_required(login_url='loginpage')
def studentview(request):
    data=StudentLogin.objects.all()
    return render(request,'teacher/studentview.html',{'data':data})
@login_required(login_url='loginpage')
def delestudent(request,id):
    StudentLogin.objects.get(id=id).delete()
    return redirect('studentview')

@login_required(login_url='loginpage')
def parentview(request):
    data=ParentLogin.objects.all()
    return render(request,'teacher/parentview.html',{'data':data})
@login_required(login_url='loginpage')
def deleparent(request,id):
    ParentLogin.objects.get(id=id).delete()
    return redirect('parentview')
@login_required(login_url='loginpage')
def tstaffmeetingview(request):
    data=StaffMeeting.objects.all()
    return render(request,'teacher/tstaffmeetingview.html',{'data':data})
@login_required(login_url='loginpage')
def tdutyview(request):
    u=TeacherLogin.objects.get(user=request.user)
    data=Duty.objects.filter(teacher=u)
    return render(request,'teacher/tdutyview.html',{'data':data})
@login_required(login_url='loginpage')
def addteacherattendance(request):
    form=teacherattendanceform()
    if request.method=='POST':
        form=teacherattendanceform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacherattendanceview')
    return render(request,'teacher/addteacherattendance.html',{'form':form})
@login_required(login_url='loginpage')
def teacherattendanceview(request):
    data=TeacherAttendance.objects.all()
    return render(request,'teacher/teacherattendanceview.html',{'data':data})
# @login_required(login_url='loginpage')
# def upteacherattendance(request,id):
#     a=TeacherAttendance.objects.get(id=id)
#     form=teacherattendanceform(instance=a)
#     if request.method=='POST':
#         form=teacherattendanceform(request.POST,instance=a)
#         if form.is_valid():
#             form.save()
#             return redirect('teacherattendanceview')
#     return render(request,'teacher/upteacherattendance.html',{'form':form})
# @login_required(login_url='loginpage')
# def deleteacherattendance(request,id):
#     TeacherAttendance.objects.get(id=id).delete()
#     return redirect('teacherattendanceview')




@login_required(login_url='loginpage')
def communitygroupview(request):
    data=CommunityGroup.objects.all()
    return render(request,'teacher/communitygroupview.html',{'data':data})
@login_required(login_url='loginpage')
def tsyllabusview(request):
    data=Syllabus.objects.all()
    return render(request,'teacher/tsyllabusview.html',{'data':data})
@login_required(login_url='loginpage')
def texamtableview(request):
    data=ExamTable.objects.all()
    return render(request,'teacher/texamtableview.html',{'data':data})
@login_required(login_url='loginpage')
def ttimetableview(request):
    data=TimeTable.objects.all()
    return render(request,'teacher/ttimetableview.html',{'data':data})

@login_required(login_url='loginpage')
def tparentsmeetingview(request):
    data=ParentsMeeting.objects.all()
    return render(request,'teacher/tparentsmeetingview.html',{'data':data})
@login_required(login_url='loginpage')
def addstudymaterial(request):
    form=studymaterial()
    if request.method=='POST':
        form=studymaterial(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('studymaterialview')
    return render(request,'teacher/addstudymaterial.html',{'form':form})
@login_required(login_url='loginpage')
def studymaterialview(request):
    data=StudyMaterial.objects.all()
    return render(request,'teacher/studymaterialview.html',{'data':data})
@login_required(login_url='loginpage')
def upstudymaterial(request,id):
    a=StudyMaterial.objects.get(id=id)
    form=studymaterial(instance=a)
    if request.method=='POST':
        form=studymaterial(request.POST,request.FILES,instance=a)
        if form.is_valid():
            form.save()
            return redirect('studymaterialview')
    return render(request,'teacher/upstudymaterial.html',{'form':form})
@login_required(login_url='loginpage')
def delestudymaterial(request,id):
    StudyMaterial.objects.get(id=id).delete()
    return redirect('studymaterialview')

@login_required(login_url='loginpage')
def addmark(request):
    form=markform()
    if request.method=='POST':
        form=markform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('markview')
    return render(request,'teacher/addmark.html',{'form':form})
@login_required(login_url='loginpage')
def markview(request):
    data=Mark.objects.all()
    return render(request,'teacher/markview.html',{'data':data})
@login_required(login_url='loginpage')
def upmark(request,id):
    a=Mark.objects.get(id=id)
    form=markform(instance=a)
    if request.method=='POST':
        form=markform(request.POST,instance=a)
        if form.is_valid():
            form.save()
            return redirect('markview')
    return render(request,'teacher/upmark.html',{'form':form})
@login_required(login_url='loginpage')
def delemark(request,id):
    Mark.objects.get(id=id).delete()
    return redirect('markview')
@login_required(login_url='loginpage')
def texamresultview(request):
    data=ExamResult.objects.all()
    return render(request,'teacher/texamresultview.html',{'data':data})
@login_required(login_url='loginpage')
def tprojectview(request):
    data=Project.objects.all()
    return render(request,'teacher/tprojectview.html',{'data':data})
@login_required(login_url='loginpage')
def addprojectmark(request,id):
    f=Project.objects.get(id=id)
    if request.method=='POST':
       r=request.POST.get('replay')
       f.replay=r
       f.save()
       return redirect('tprojectview')
    return render(request,'teacher/addprojectmark.html',{'f':f})

@login_required(login_url='loginpage')
def tassignmentview(request):
    data=Assignment.objects.all()
    return render(request,'teacher/tassignmentview.html',{'data':data})
@login_required(login_url='loginpage')
def addassignmentmark(request,id):
    f=Assignment.objects.get(id=id)
    if request.method=='POST':
       r=request.POST.get('replay')
       f.replay=r
       f.save()
       return redirect('tassignmentview')
    return render(request,'teacher/addassignmentmark.html',{'f':f})


@login_required(login_url='loginpage')
def tseminarview(request):
    data=Seminar.objects.all()
    return render(request,'teacher/tseminarview.html',{'data':data})
@login_required(login_url='loginpage')
def addseminarmark(request,id):
    f=Seminar.objects.get(id=id)
    if request.method=='POST':
       r=request.POST.get('replay')
       f.replay=r
       f.save()
       return redirect('tseminarview')
    return render(request,'teacher/addseminarmark.html',{'f':f})

@login_required(login_url='loginpage')
def thwview(request):
    data=Hw.objects.all()
    return render(request,'teacher/thwview.html',{'data':data})
@login_required(login_url='loginpage')
def addhwmark(request,id):
    f=Hw.objects.get(id=id)
    if request.method=='POST':
       r=request.POST.get('replay')
       f.replay=r
       f.save()
       return redirect('thwview')
    return render(request,'teacher/addhwmark.html',{'f':f})
@login_required(login_url='loginpage')
def join_community(request, id):
    s = CommunityGroup.objects.get(id=id)
    c = TeacherLogin.objects.get(user=request.user)
    print(c)
    appointment = Appointment.objects.filter(user=c, schedule=s)
    if appointment.exists():
        messages.info(request, 'You Have Already Requested Appointment for this Schedule')
        return redirect('communitygroupview')
    else:
        if request.method == 'POST':
            obj = Appointment()
            obj.user = c
            obj.schedule = s
            obj.save()
            messages.info(request, 'Appointment Booked Successfully')
            return redirect('appointment_view')
    return render(request, 'teacher/take_appointment.html', {'schedule': s})


@login_required(login_url='loginpage')
def appointment_view(request):
    c = TeacherLogin.objects.get(user=request.user)
    a = Appointment.objects.filter(user=c)
    return render(request, 'teacher/appointment_view.html', {'appointment': a})
@login_required(login_url='loginpage')
def appointment_teacher(request):
    a = StudentAppointment.objects.all()
    context = {
        'studentappointment': a,
    }
    return render(request, 'teacher/studentappoinments.html', context)
@login_required(login_url='loginpage')
def tapprove_appointment(request, id):
    a = StudentAppointment.objects.get(id=id)
    a.status = 1
    a.save()
    messages.info(request, 'Appointment  Confirmed')
    return redirect('appointment_teacher')
@login_required(login_url='loginpage')
def treject_appointment(request, id):
    n = StudentAppointment.objects.get(id=id)
    n.status = 2
    n.save()
    messages.info(request, 'Appointment Rejected')
    return redirect('appointment_teacher')

@login_required(login_url='loginpage')
def appointment_parent(request):
    a = ParentAppointment.objects.all()
    context = {
        'parentappointment': a,
    }
    return render(request, 'teacher/parentappoinments.html', context)
@login_required(login_url='loginpage')
def papprove_appointment(request, id):
    a = ParentAppointment.objects.get(id=id)
    a.status = 1
    a.save()
    messages.info(request, 'Appointment  Confirmed')
    return redirect('appointment_parent')
@login_required(login_url='loginpage')
def preject_appointment(request, id):
    n = ParentAppointment.objects.get(id=id)
    n.status = 2
    n.save()
    messages.info(request, 'Appointment Rejected')
    return redirect('appointment_parent')
@login_required(login_url='loginpage')
def tpcomplaintview(request):
    data=ParentComplaint.objects.all()
    return render(request,'teacher/tpcomplaintview.html',{'data':data})
@login_required(login_url='loginpage')
def addpreplay(request,id):
    f=ParentComplaint.objects.get(id=id)
    if request.method=='POST':
       r=request.POST.get('replay')
       f.replay=r
       f.save()
       return redirect('tpcomplaintview')
    return render(request,'teacher/addpreplay.html',{'f':f})
@login_required(login_url='loginpage')
def tscomplaintview(request):
    data=Complaint.objects.all()
    return render(request,'teacher/tscomplaintview.html',{'data':data})
@login_required(login_url='loginpage')
def addsreplay(request,id):
    f=Complaint.objects.get(id=id)
    if request.method=='POST':
       r=request.POST.get('replay')
       f.replay=r
       f.save()
       return redirect('tscomplaintview')
    return render(request,'teacher/addsreplay.html',{'f':f})

@login_required(login_url='loginpage')
def addtschat(request):
    form=schatform()
    u=request.user
    if request.method=='POST':
        form=schatform(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
            return redirect('tschatview')
    return render(request,'teacher/addtschat.html',{'form':form})
@login_required(login_url='loginpage')
def tschatview(request):
    data=Schat.objects.all()
    return render(request,'teacher/tschatview.html',{'data':data})


@login_required(login_url='loginpage')
def addtpchat(request):
    form=pchatform()
    u=request.user
    if request.method=='POST':
        form=pchatform(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
            return redirect('tpchatview')
    return render(request,'teacher/addtpchat.html',{'form':form})
@login_required(login_url='loginpage')
def tpchatview(request):
    data=Pchat.objects.all()
    return render(request,'teacher/tpchatview.html',{'data':data})

@login_required(login_url='loginpage')
def addnotification(request):
    form = notificationform()
    if request.method == 'POST':
        form = notificationform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('anotificationview')
    return render(request, 'teacher/addnotification.html', {'form': form})
@login_required(login_url='loginpage')
def anotificationview(request):
    data=Notification.objects.all()
    return render(request,'teacher/anotificationview.html',{'data':data})


@login_required(login_url='loginpage')
def upnotification(request,id):
    a=Notification.objects.get(id=id)
    form=notificationform(instance=a)
    if request.method=='POST':
        form=notificationform(request.POST,instance=a)
        if form.is_valid():
            form.save()
            return redirect('anotificationview')
    return render(request,'teacher/upnotification.html',{'form':form})
@login_required(login_url='loginpage')
def delenotification(request,id):
    Notification.objects.get(id=id).delete()
    return redirect('anotificationview')
@login_required(login_url='loginpage')
def tpay_history_view(request):
    data=Notification.objects.all()
    return render(request,'student/spayment_history_view.html',{'data':data})










