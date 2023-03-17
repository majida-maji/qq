from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, redirect


# Create your views here.
from myschoolapp.forms import LoginReg, TeacherReg, StudentReg, ParentReg, courseform


def index(request):
    return render(request,'home.html')

def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('adindex')
            elif user.is_teacher:
                return redirect('tindex')
            elif user.is_student:
                return redirect('sindex')
            elif user.is_parent:
                return redirect('pindex')
        else:
            messages.info(request,"user is not found")
    return render(request,'login.html')


def logoutview(request):
    logout(request)
    messages.info(request,"logout successsfully!")
    return  redirect("loginpage")

def treg(request):
    user_form=LoginReg()
    teacher_form=TeacherReg()
    if request.method=='POST':
        user_form=LoginReg(request.POST)
        teacher_form=TeacherReg(request.POST)
        if user_form.is_valid() and teacher_form.is_valid():
            user=user_form.save(commit=False)
            user.is_teacher=True
            user.save()
            teacher=teacher_form.save(commit=False)
            teacher.user=user
            teacher.save()
            messages.info(request,"sucessfully registered")
            return redirect('loginpage')
    return render(request,'treg.html',{'user_form':user_form,'teacher_form':teacher_form})


def sreg(request):
    user_form=LoginReg()
    student_form=StudentReg()
    if request.method=='POST':
        user_form=LoginReg(request.POST)
        student_form=StudentReg(request.POST)
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save(commit=False)
            user.is_student = True
            user.save()
            student = student_form.save(commit=False)
            student.user = user
            student.save()
            messages.info(request, "sucessfully registered")
            return redirect('loginpage')
    return render(request,'sreg.html',{'user_form':user_form,'student_form':student_form})


def preg(request):
    user_form = LoginReg()
    parent_form = ParentReg()
    if request.method == 'POST':
        user_form = LoginReg(request.POST)
        parent_form = ParentReg(request.POST)
        if user_form.is_valid() and parent_form.is_valid():
            user = user_form.save(commit=False)
            user.is_parent = True
            user.save()
            parent = parent_form.save(commit=False)
            parent.user = user
            parent.save()
            messages.info(request, "sucessfully registered")
            return redirect('loginpage')
    return render(request,'preg.html',{'user_form':user_form,'parent_form':parent_form})




def adindex(request):

    return render(request,'adindex.html')

def tindex(request):
    return render(request,'tindex.html')

def sindex(request):
    return render(request,'sindex.html')

def pindex(request):
    return render(request,'pindex.html')

def tcgindex(request):
    return render(request,'tcgindex.html')

def scgindex(request):
    return render(request,'scgindex.html')

def pcgindex(request):
    return render(request,'pcgindex.html')


