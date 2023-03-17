import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

import myschool
from myschoolapp.forms import courseform, syllabusform, timetableform, examtableform, dutyform, examresultform, \
    staffmeetingform, parentsmeetingform, communitygroupform, notificationform, teacherattendanceform
from myschoolapp.models import TeacherLogin, Course, Syllabus, TimeTable, ExamTable, Duty, ExamResult, StaffMeeting, \
    ParentsMeeting, CommunityGroup, Appointment, ParentComplaint, Complaint, Notification, TeacherAttendance


@login_required(login_url='loginpage')
def teacherview(request):
    data=TeacherLogin.objects.all()
    return render(request,'admin/teacherview.html',{'data':data})

@login_required(login_url='loginpage')
def dele(request,id):
    TeacherLogin.objects.get(id=id).delete()
    return redirect('teacherview')



@login_required(login_url='loginpage')
def teacherat(request):
    data = TeacherLogin.objects.all()
    return render(request, 'admin/teacherat.html',{'data': data})


# @login_required(login_url='loginpage')
# def addteacherattendence(request):
#     form =teacherattendanceform
#     if request.method == 'POST':
#         form = teacherattendanceform(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('courseview')
#     return render(request,'admin/addcourse.html',{'form':form})

now = datetime.datetime.now()
@login_required(login_url='loginpage')
def mark(request, id):
    user = TeacherLogin.objects.get(id=id)
    att = TeacherAttendance.objects.filter(teacher=user, date=datetime.date.today())
    if att.exists():
        messages.info(request, "Today's Attendance Already marked for this Student ")
        return redirect('teacherat')
    else:
        if request.method == 'POST':
            attndc = request.POST.get('attendance')
            TeacherAttendance(teacher=user, date=datetime.date.today(), attendance=attndc,time=now.time()).save()
            messages.info(request, "Attendance Added successfully ")
            return redirect('teacherat')
    return render(request, 'admin/addteacherattendence.html')

@login_required(login_url='accounts:login_view')
def view_attendance(request):
    value_list = TeacherAttendance.objects.values_list('date', flat=True).distinct()
    attendance= {}
    for value in value_list:
        attendance[value] = TeacherAttendance.objects.filter(date=value)
    return render(request, 'admin/view_attendance.html', {'attendanse':attendance})
#
@login_required(login_url='accounts:login_view')
def day_attendance(request, date):
    attendance = TeacherAttendance.objects.filter(date=date)
    context = {
        'attendances': attendance,
        'date': date
    }
    return render(request, 'admin/day_attendance.html', context)




@login_required(login_url='loginpage')
def addcourse(request):
    form = courseform()
    if request.method == 'POST':
        form = courseform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courseview')
    return render(request,'admin/addcourse.html',{'form':form})


@login_required(login_url='loginpage')
def courseview(request):
    data=Course.objects.all()
    return render(request,'admin/courseview.html',{'data':data})
@login_required(login_url='loginpage')
def upcourse(request,id):
    a=Course.objects.get(id=id)
    form=courseform(instance=a)
    if request.method=='POST':
        form=courseform(request.POST,instance=a)
        if form.is_valid():
            form.save()
            return redirect('courseview')
    return render(request,'admin/upcourse.html',{'form':form})

@login_required(login_url='loginpage')
def delecourse(request,id):
    Course.objects.get(id=id).delete()
    return redirect('courseview')
@login_required(login_url='loginpage')
def addsyllabus(request):
    form=syllabusform()
    if request.method=='POST':
        form=syllabusform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('syllabusview')
    return render(request,'admin/addsyllabus.html',{'form':form})
@login_required(login_url='loginpage')
def syllabusview(request):
    data=Syllabus.objects.all()
    return render(request,'admin/syllabusview.html',{'data':data})
@login_required(login_url='loginpage')
def upsyllabus(request,id):
    a=Syllabus.objects.get(id=id)
    form=syllabusform(instance=a)
    if request.method=='POST':
        form=syllabusform(request.POST,request.FILES,instance=a)
        if form.is_valid():
            form.save()
            return redirect('syllabusview')
    return render(request,'admin/upsyllabus.html',{'form':form})
@login_required(login_url='loginpage')
def delesyllabus(request,id):
    Syllabus.objects.get(id=id).delete()
    return redirect('syllabusview')
@login_required(login_url='loginpage')
def addtimetable(request):
    form=timetableform()
    if request.method=='POST':
        form=timetableform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('timetableview')
    return render(request,'admin/addtimetable.html',{'form':form})
@login_required(login_url='loginpage')
def timetableview(request):
    data=TimeTable.objects.all()
    return render(request,'admin/timetableview.html',{'data':data})

@login_required(login_url='loginpage')
def uptimetable(request,id):
    a=TimeTable.objects.get(id=id)
    form=timetableform(instance=a)
    if request.method=='POST':
        form=timetableform(request.POST,instance=a)
        if form.is_valid():
            form.save()
            return redirect('timetableview')
    return render(request,'admin/uptimetable.html',{'form':form})

@login_required(login_url='loginpage')
def deletimetable(request,id):
    TimeTable.objects.get(id=id).delete()
    return redirect('timetableview')

@login_required(login_url='loginpage')
def addexamtable(request):
    form = examtableform()
    if request.method == 'POST':
        form = examtableform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('examtableview')
    return render(request, 'admin/addexamtable.html', {'form': form})
@login_required(login_url='loginpage')
def examtableview(request):
    data=ExamTable.objects.all()
    return render(request,'admin/examtableview.html',{'data':data})
@login_required(login_url='loginpage')
def upexamtable(request,id):
    a=ExamTable.objects.get(id=id)
    form=examtableform(instance=a)
    if request.method=='POST':
        form=examtableform(request.POST,request.FILES,instance=a)
        if form.is_valid():
            form.save()
            return redirect('examtableview')
    return render(request,'admin/upexamtable.html',{'form':form})
@login_required(login_url='loginpage')
def deleexamtable(request,id):
    ExamTable.objects.get(id=id).delete()
    return redirect('examtableview')
@login_required(login_url='loginpage')
def addduty(request):
    form=dutyform()
    if request.method=='POST':
        form=dutyform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dutyview')
    return render(request,'admin/addduty.html',{'form':form})
@login_required(login_url='loginpage')
def dutyview(request):
    data=Duty.objects.all()
    return render(request,'admin/dutyview.html',{'data':data})
@login_required(login_url='loginpage')
def upduty(request,id):
    a=Duty.objects.get(id=id)
    form=dutyform(instance=a)
    if request.method=='POST':
        form=dutyform(request.POST,instance=a)
        if form.is_valid():
            form.save()
            return redirect('dutyview')
    return render(request,'admin/upduty.html',{'form':form})
@login_required(login_url='loginpage')
def deleduty(request,id):
    Duty.objects.get(id=id).delete()
    return redirect('dutyview')
@login_required(login_url='loginpage')
def addexamresult(request):
    form =examresultform()
    if request.method == 'POST':
        form = examresultform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('examresultview')
    return render(request, 'admin/addexamresult.html', {'form': form})

@login_required(login_url='loginpage')
def examresultview(request):
    data=ExamResult.objects.all()
    return render(request,'admin/examresultview.html',{'data':data})

@login_required(login_url='loginpage')
def upexamresult(request,id):
    a=ExamResult.objects.get(id=id)
    form=examresultform(instance=a)
    if request.method=='POST':
        form=examresultform(request.POST,request.FILES,instance=a)
        if form.is_valid():
            form.save()
            return redirect('examresultview')
    return render(request,'admin/upexamresult.html',{'form':form})
@login_required(login_url='loginpage')
def deleexamresult(request,id):
    ExamResult.objects.get(id=id).delete()
    return redirect('examresultview')


@login_required(login_url='loginpage')
def addstaffmeeting(request):
    form = staffmeetingform()
    if request.method == 'POST':
        form = staffmeetingform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staffmeetingview')
    return render(request, 'admin/addstaffmeeting.html', {'form': form})

@login_required(login_url='loginpage')
def staffmeetingview(request):
    data=StaffMeeting.objects.all()
    return render(request,'admin/staffmeetingview.html',{'data':data})
@login_required(login_url='loginpage')
def upstaffmeeting(request,id):
    a=StaffMeeting.objects.get(id=id)
    form=staffmeetingform(instance=a)
    if request.method=='POST':
        form=staffmeetingform(request.POST,instance=a)
        if form.is_valid():
            form.save()
            return redirect('staffmeetingview')
    return render(request,'admin/upstaffmeeting.html',{'form':form})
@login_required(login_url='loginpage')
def delestaffmeeting(request,id):
    StaffMeeting.objects.get(id=id).delete()
    return redirect('staffmeetingview')

@login_required(login_url='loginpage')
def addparentsmeeting(request):
    form = parentsmeetingform()
    if request.method == 'POST':
        form = parentsmeetingform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parentsmeetingview')
    return render(request, 'admin/addparentsmeeting.html', {'form': form})


@login_required(login_url='loginpage')
def parentsmeetingview(request):
    data=ParentsMeeting.objects.all()
    return render(request,'admin/parentsmeetingview.html',{'data':data})
@login_required(login_url='loginpage')
def upparentsmeeting(request,id):
    a=ParentsMeeting.objects.get(id=id)
    form=parentsmeetingform(instance=a)
    if request.method=='POST':
        form=parentsmeetingform(request.POST,instance=a)
        if form.is_valid():
            form.save()
            return redirect('parentsmeetingview')
    return render(request,'admin/upparentsmeeting.html',{'form':form})
@login_required(login_url='loginpage')
def deleparentsmeeting(request,id):
    ParentsMeeting.objects.get(id=id).delete()
    return redirect('parentsmeetingview')

@login_required(login_url='loginpage')
def addcommunitygroup(request):
    form = communitygroupform()
    if request.method == 'POST':
        form = communitygroupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admincommunitygroupview')
    return render(request, 'admin/addcommunitygroup.html', {'form': form})
@login_required(login_url='loginpage')
def admincommunitygroupview(request):
    data=CommunityGroup.objects.all()
    return render(request,'admin/communitygroupview.html',{'data':data})


@login_required(login_url='loginpage')
def upcommunitygroup(request,id):
    a=CommunityGroup.objects.get(id=id)
    form=communitygroupform(instance=a)
    if request.method=='POST':
        form=communitygroupform(request.POST,instance=a)
        if form.is_valid():
            form.save()
            return redirect('admincommunitygroupview')
    return render(request,'admin/upcommunitygroup.html',{'form':form})
@login_required(login_url='loginpage')
def delecommunitygroup(request,id):
    CommunityGroup.objects.get(id=id).delete()
    return redirect('admincommunitygroupview')
@login_required(login_url='loginpage')
def managecommunitygroup(request):
    data=CommunityGroup.objects.all()
    return render(request,'admin/managecommunitygroup.html',{'data':data})
@login_required(login_url='loginpage')
def appointment_admin(request):
    a = Appointment.objects.all()
    context = {
        'appointment': a,
    }
    return render(request, 'admin/appointments.html', context)
@login_required(login_url='loginpage')
def approve_appointment(request, id):
    a = Appointment.objects.get(id=id)
    a.status = 1
    a.save()
    messages.info(request, 'Appointment  Confirmed')
    return redirect('appointment_admin')
@login_required(login_url='loginpage')
def reject_appointment(request, id):
    n = Appointment.objects.get(id=id)
    n.status = 2
    n.save()
    messages.info(request, 'Appointment Rejected')
    return redirect('appointment_admin')
@login_required(login_url='loginpage')
def apcomplaintview(request):
    data=ParentComplaint.objects.all()
    return render(request,'admin/apcomplaintview.html',{'data':data})
@login_required(login_url='loginpage')
def ascomplaintview(request):
    data=Complaint.objects.all()
    return render(request,'admin/ascomplaintview.html',{'data':data})

@login_required(login_url='loginpage')
def apayment_history_view(request):
    data=Notification.objects.all()
    return render(request,'admin/apayment_history_view.html',{'data':data})











def payment_details(request):
    data=Notification.objects.all()
    return render(request,'admin/payment_details.html',{'data':data})





# def addbill(request):
#     form=addbillform()
#     if request.method=="POST":
#         form=addbillform(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('viewbill')
#     return render(request,'admin/addbill.html',{'form':form})
#
# def viewbill(request):
#     data=Bill.objects.all()
#     return render(request,'admin/viewbill.html',{'data':data})
#


