from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_teacher=models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)
    is_parent=models.BooleanField(default=False)

class TeacherLogin(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE,related_name='teacher')

    name=models.CharField(max_length=30)
    age=models.IntegerField()
    gender=models.CharField(max_length=30)
    location=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone_no=models.IntegerField()
    email=models.EmailField()
    qualification=models.CharField(max_length=100)
    department=models.CharField(max_length=100)

    def __str__(self):
        return self.name







class StudentLogin(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE,related_name='student')

    name=models.CharField(max_length=30)
    age=models.IntegerField()
    gender=models.CharField(max_length=30)
    location=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone_no=models.IntegerField()
    email=models.EmailField()
    parent_name=models.CharField(max_length=100)
    parent_phn_no=models.IntegerField()
    department=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}" \
               f"----{self.email}"





class ParentLogin(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE,related_name='parent')
    name=models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    email = models.EmailField()

    s_name = models.ForeignKey(StudentLogin,on_delete=models.CASCADE)
    department = models.CharField(max_length=10)

    def __str__(self):
        return self.name




class Course(models.Model):
    course_name=models.CharField(max_length=200)
    department=models.CharField(max_length=200)
    explanation=models.CharField(max_length=200)
    course_duration=models.CharField(max_length=200)

    def __str__(self):
        return self.course_name



class Syllabus(models.Model):
    date=models.DateField(auto_now=True)
    add_syllabus=models.FileField(upload_to='syllabus')

    def __str__(self):
        return self.add_syllabus



class TimeTable(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    department=models.CharField(max_length=200)
    mon=models.CharField(max_length=200)
    tue=models.CharField(max_length=200)
    wed=models.CharField(max_length=200)
    thu=models.CharField(max_length=200)
    fri=models.CharField(max_length=200)



class ExamTable(models.Model):
    date=models.DateField(auto_now=True)
    add_timetable=models.FileField(upload_to='timetable')


class Duty(models.Model):
    teacher=models.ForeignKey(TeacherLogin,on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    department=models.CharField(max_length=200)


class ExamResult(models.Model):
    student=models.ForeignKey(StudentLogin,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    department=models.CharField(max_length=200)
    result=models.FileField(upload_to='result')

class StaffMeeting(models.Model):
    date=models.DateField()
    time=models.TimeField()
    content=models.CharField(max_length=200)

class ParentsMeeting(models.Model):
    date=models.DateField()
    time=models.TimeField()
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    department=models.CharField(max_length=200)
    content=models.CharField(max_length=200)


class CommunityGroup(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    department = models.CharField(max_length=200)
    status = models.IntegerField(default=0)


class TeacherAttendance(models.Model):
    teacher = models.ForeignKey(TeacherLogin, on_delete=models.CASCADE,null=True,blank=True,related_name='attendance')
    student = models.ForeignKey(StudentLogin, on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateField()
    time = models.TimeField()
    attendance=models.CharField(max_length=21)

    def __str__(self):
        return self.attendance

class StudyMaterial(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    department = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    studymaterial = models.FileField(upload_to='studymaterial')


class Mark(models.Model):
    student=models.ForeignKey(StudentLogin,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    department=models.CharField(max_length=200)
    s1=models.IntegerField()
    s2=models.IntegerField()
    s3=models.IntegerField()
    s4=models.IntegerField()
    s5=models.IntegerField()
    s6=models.IntegerField()
    status=models.IntegerField(default=0)
    total=models.IntegerField(default=0)

    def total(self):
        self.total=self.s1+self.s2+self.s3+self.s4+self.s5+self.s6
        return self.total

class Note(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    department = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    subject=models.CharField(max_length=200)
    note = models.FileField(upload_to='studymaterial')


class Complaint(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    department = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    complaint=models.TextField(max_length=10000)
    replay = models.TextField(null=True, blank=True)


class Project(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    department = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    subject=models.CharField(max_length=200)
    project = models.FileField(upload_to='project')
    replay = models.TextField(null=True, blank=True)


class Assignment(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    department = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    subject=models.CharField(max_length=200)
    assignment = models.FileField(upload_to='assignment')
    replay = models.TextField(null=True, blank=True)


class Seminar(models.Model):
    user=models.ForeignKey(Login,on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    department = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    subject=models.CharField(max_length=200)
    seminar = models.FileField(upload_to='seminar')
    replay=models.TextField(null=True,blank=True)


class Hw(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    department = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    subject=models.CharField(max_length=200)
    hw = models.FileField(upload_to='hw')
    replay = models.TextField(null=True, blank=True)


class Appointment(models.Model):
    user = models.ForeignKey(TeacherLogin, on_delete=models.CASCADE, related_name='appointment')
    schedule = models.ForeignKey(CommunityGroup, on_delete=models.CASCADE)
    department = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)

    status = models.IntegerField(default=0)


class StudentAppointment(models.Model):
    user = models.ForeignKey(StudentLogin, on_delete=models.CASCADE, related_name='studentappointment')
    schedule = models.ForeignKey(CommunityGroup, on_delete=models.CASCADE)
    department = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    status = models.IntegerField(default=0)


class ParentAppointment(models.Model):
    user = models.ForeignKey(ParentLogin, on_delete=models.CASCADE, related_name='parentappointment')
    student = models.ForeignKey(StudentLogin, on_delete=models.CASCADE,null=True)
    schedule = models.ForeignKey(CommunityGroup, on_delete=models.CASCADE)
    department = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.user


class ParentComplaint(models.Model):
    user=models.ForeignKey(Login,on_delete=models.CASCADE)
    student = models.ForeignKey(StudentLogin, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    department = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    complaint=models.TextField(max_length=10000)
    replay=models.TextField(null=True,blank=True)




class Schat(models.Model):
    user=models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    chat=models.TextField(max_length=100000)
    date=models.DateField(auto_now=True)
    time=models.TimeField(auto_now=True)


class Pchat(models.Model):
    user=models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    chat=models.TextField(max_length=100000)
    date=models.DateField(auto_now=True)
    time=models.TimeField(auto_now=True)



class Notification(models.Model):

    name_and_email=models.ForeignKey(StudentLogin,on_delete=models.CASCADE,null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    department = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    last_date=models.DateField(null=True)
    notification=models.TextField(max_length=10000)
    amount=models.IntegerField()
    paid_on=models.DateField(auto_now=True)
    status=models.IntegerField(default=0)
    def __str__(self):
        return f"{self.name_and_email.name}----{self.name_and_email.email}"
    def __int__(self):
        return self.amount


class DirectPay(models.Model):
    card_no=models.IntegerField()
    cvv=models.IntegerField()
    amount=models.IntegerField()
    status=models.IntegerField(default=0)



class Bill(models.Model):
    name=models.ForeignKey(ParentLogin,on_delete=models.CASCADE)
    bill_date=models.DateTimeField(auto_now=True)
    amount=models.IntegerField()
    paid_on=models.DateField(auto_now=True)
    status=models.IntegerField(default=0)




# class Payment(models.Model):
#     user = models.ForeignKey(Login, on_delete=models.CASCADE,null=True)
#     student = models.ForeignKey(StudentLogin, on_delete=models.CASCADE,null=True)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     department = models.CharField(max_length=200)
#     date = models.DateField(auto_now=True)
#     pay = models.TextField(null=True, blank=True)
#
#
#
#
class OnlinePayment(models.Model):
    parent=models.ForeignKey(ParentLogin,on_delete=models.CASCADE,null=True)
    card_no=models.CharField(max_length=200,null=True)
    cvv=models.CharField(max_length=200)
    exp_date=models.DateField(null=True)
    amount=models.IntegerField()
#
class Bill(models.Model):
    name=models.ForeignKey(ParentLogin,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    amount=models.IntegerField()
    payed_on=models.DateField(auto_now=True)
    status=models.IntegerField(default=0)







