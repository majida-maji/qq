from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from myschoolapp.forms import complaintform, parentcomplaintform, notificationform, pchatform, directpayform, \
    onlinepaymentform
from myschoolapp.models import Mark, ExamTable, TimeTable, ExamResult, ParentsMeeting, CommunityGroup, ParentLogin, \
    ParentAppointment, Complaint, ParentComplaint, Notification, Pchat, Bill, OnlinePayment

@login_required(login_url='loginpage')
def pmarkview(request):
    data=Mark.objects.all()
    return render(request,'parent/pmarkview.html',{'data':data})
@login_required(login_url='loginpage')
def pexamtableview(request):
    data=ExamTable.objects.all()
    return render(request,'parent/pexamtableview.html',{'data':data})
@login_required(login_url='loginpage')
def ptimetableview(request):
    data=TimeTable.objects.all()
    return render(request,'parent/ptimetableview.html',{'data':data})
@login_required(login_url='loginpage')
def pexamresultview(request):
    data=ExamResult.objects.all()
    return render(request,'parent/pexamresultview.html',{'data':data})
@login_required(login_url='loginpage')
def pparentsmeetingview(request):
    data=ParentsMeeting.objects.all()
    return render(request,'parent/pparentsmeetingview.html',{'data':data})
@login_required(login_url='loginpage')
def pcommunitygroupview(request):
    data=CommunityGroup.objects.all()
    return render(request,'parent/pcommunitygroupview.html',{'data':data})
@login_required(login_url='loginpage')
def pjoin_community(request, id):
    s = CommunityGroup.objects.get(id=id)
    c = ParentLogin.objects.get(user=request.user)
    print(c)
    appointment = ParentAppointment.objects.filter(user=c,schedule=s)
    if appointment.exists():
        messages.info(request, 'You Have Already Requested Appointment for this Schedule')
        return redirect('pcommunitygroupview')
    else:
        if request.method == 'POST':
            obj = ParentAppointment()
            obj.user = c
            obj.schedule = s
            obj.save()
            messages.info(request, 'Appointment Booked Successfully')
            return redirect('pappointment_view')
    return render(request, 'parent/take_pappointment.html', {'schedule': s})
@login_required(login_url='loginpage')
def pappointment_view(request):
    c = ParentLogin.objects.get(user=request.user)
    a = ParentAppointment.objects.filter(user=c)
    return render(request, 'parent/pappointment_view.html', {'appointment': a})

@login_required(login_url='loginpage')
def paddcomplaint(request):
    form=parentcomplaintform()
    u=request.user
    if request.method=='POST':
        form=parentcomplaintform(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
            return redirect('pcomplaintview')
    return render(request,'parent/paddcomplaint.html',{'form':form})
@login_required(login_url='loginpage')
def pcomplaintview(request):
    data=ParentComplaint.objects.filter(user=request.user)
    return render(request,'parent/pcomplaintview.html',{'data':data})
@login_required(login_url='loginpage')
def pupcomplaint(request,id):
    a=ParentComplaint.objects.get(id=id)
    form=parentcomplaintform(instance=a)
    if request.method=='POST':
        form=parentcomplaintform(request.POST,instance=a)
        if form.is_valid():
            form.save()
            return redirect('pcomplaintview')
    return render(request,'parent/pupcomplaint.html',{'form':form})
@login_required(login_url='loginpage')
def pdelecomplaint(request,id):
    ParentComplaint.objects.get(id=id).delete()
    return redirect('pcomplaintview')
@login_required(login_url='loginpage')
def pnotificationview(request):
    u=ParentLogin.objects.get(user=request.user)

    data=Notification.objects.filter(name_and_email=u.s_name)
    return render(request,'parent/pnotificationview.html',{'data':data})
@login_required(login_url='loginpage')
def pay_bill(request,id):
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
        return redirect('pnotificationview')
    return render(request,'parent/paybill.html')
@login_required(login_url='loginpage')
def pay_in_direct(request, id):
    bi = Notification.objects.get(id=id)
    bi.status = 2
    bi.save()
    messages.info(request, 'Choosed to Pay Fee Direct in office')
    return redirect('pnotificationview')

@login_required(login_url='loginpage')
def bill_history(request):
    u = Notification.objects.get(user=request.user)
    bill = Bill.objects.filter(name=u, status__in=[1, 2])

    return render(request, 'parent/view_bill_history.html', {'bills': bill})

@login_required(login_url='loginpage')
def pay_history_view(request):
    data=Notification.objects.all()
    return render(request,'parent/payment_history_view.html',{'data':data})

@login_required(login_url='loginpage')
def viewdetails(request):
    data=Notification.objects.all()
    return render(request,'parent/viewdetails.html',{'data':data})

@login_required(login_url='loginpage')
def addpchat(request):
    form=pchatform()
    u=request.user
    if request.method=='POST':
        form=pchatform(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
            return redirect('pchatview')
    return render(request,'parent/addpchat.html',{'form':form})
@login_required(login_url='loginpage')
def pchatview(request):
    data=Pchat.objects.all()
    return render(request,'parent/pchatview.html',{'data':data})



