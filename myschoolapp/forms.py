from django import forms
from django.contrib.auth.forms import UserCreationForm


from myschoolapp.models import Login, TeacherLogin, StudentLogin, ParentLogin, Course, Syllabus, TimeTable, ExamTable, \
    Duty, ExamResult, StaffMeeting, ParentsMeeting, CommunityGroup, TeacherAttendance, StudyMaterial, Mark, Note, \
    Complaint, Project, Assignment, Seminar, Hw, ParentComplaint, Notification, Schat, Pchat, Bill, DirectPay, \
    OnlinePayment


class LoginReg(UserCreationForm):
    class Meta:
        model=Login
        fields=('username','password1','password2')

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class TeacherReg(forms.ModelForm):
    class Meta:
        model=TeacherLogin
        exclude=('user',)


class StudentReg(forms.ModelForm):
    class Meta:
        model=StudentLogin
        exclude=('user',)


class ParentReg(forms.ModelForm):
    class Meta:
        model=ParentLogin
        exclude=('user',)


class courseform(forms.ModelForm):
    class Meta:
        model=Course
        fields='__all__'

dep_choice=(
    ('..','..'),
    ('bca','bca'),
    ('mca','mca')
)
class timetableform(forms.ModelForm):
    department=forms.ChoiceField(choices=dep_choice)
    class Meta:
        model=TimeTable
        fields='__all__'

class syllabusform(forms.ModelForm):
    class Meta:
        model=Syllabus
        fields='__all__'


class examtableform(forms.ModelForm):
    class Meta:
        model=ExamTable
        fields='__all__'

class dutyform(forms.ModelForm):
    date=forms.DateField(widget=DateInput)
    time=forms.TimeField(widget=TimeInput)
    department=forms.ChoiceField(choices=dep_choice)
    class Meta:
        model=Duty
        fields='__all__'


class examresultform(forms.ModelForm):
    department=forms.ChoiceField(choices=dep_choice)
    class Meta:
        model=ExamResult
        fields='__all__'


class staffmeetingform(forms.ModelForm):
    date=forms.DateField(widget=DateInput)
    time=forms.TimeField(widget=TimeInput)
    class Meta:
        model=StaffMeeting
        fields='__all__'

class parentsmeetingform(forms.ModelForm):
    department=forms.ChoiceField(choices=dep_choice)
    date=forms.DateField(widget=DateInput)
    time=forms.TimeField(widget=TimeInput)
    class Meta:
        model=ParentsMeeting
        fields='__all__'


class communitygroupform(forms.ModelForm):
    department=forms.ChoiceField(choices=dep_choice)
    class Meta:
        model=CommunityGroup
        exclude=('status',)
at_choice=(

    ('yes','yes'),
    ('no','no')
)
class teacherattendanceform(forms.ModelForm):
    attendance=forms.ChoiceField(choices=at_choice,required=True,widget=forms.RadioSelect)
    class Meta:
        model =TeacherAttendance
        exclude=('attendance','teacher','student',)

class studymaterial(forms.ModelForm):
    department = forms.ChoiceField(choices=dep_choice)
    class Meta:
        model=StudyMaterial
        fields='__all__'

class markform(forms.ModelForm):
    department=forms.ChoiceField(choices=dep_choice)
    class Meta:
        model=Mark
        exclude=('status',)

class noteform(forms.ModelForm):
    department = forms.ChoiceField(choices=dep_choice)
    class Meta:
        model=Note
        fields='__all__'

class complaintform(forms.ModelForm):
    department = forms.ChoiceField(choices=dep_choice)
    class Meta:
        model=Complaint
        exclude=('user','replay',)

class projectform(forms.ModelForm):
    department = forms.ChoiceField(choices=dep_choice)
    class Meta:
        model=Project
        exclude=('user','replay',)

class assignmentform(forms.ModelForm):
    department = forms.ChoiceField(choices=dep_choice)
    class Meta:
        model=Assignment
        exclude=('user','replay',)


class seminarform(forms.ModelForm):
    department = forms.ChoiceField(choices=dep_choice)
    class Meta:
        model=Seminar
        exclude = ('user','replay',)

class hwform(forms.ModelForm):
    department = forms.ChoiceField(choices=dep_choice)
    class Meta:
        model=Hw
        exclude=('user','replay',)


class parentcomplaintform(forms.ModelForm):
    department = forms.ChoiceField(choices=dep_choice)
    class Meta:
        model=ParentComplaint
        exclude=('user','replay',)


class notificationform(forms.ModelForm):
    last_date=forms.DateField(widget=DateInput)
    department = forms.ChoiceField(choices=dep_choice)

    class Meta:
        model=Notification
        exclude=('user','pay','status','student_name','paid_on',)


class directpayform(forms.ModelForm):
    class Meta:
        model=DirectPay
        exclude=('status',)


class billform(forms.ModelForm):
    class Meta:
        model=Bill
        exclude=('status','paid_on',)

# class paymentform(forms.ModelForm):
#
#     department = forms.ChoiceField(choices=dep_choice)
#     class Meta:
#         model=Payment
#         exclude=('user','pay','status',)
#
# class addbillform(forms.ModelForm):
#     class Meta:
#         model=Bill
#         exclude=('status','payed_on',)
#
# class adddetailsform(forms.ModelForm):
#     department=forms.ChoiceField(choices=dep_choice)
#     class Meta:
#         model=Notification
#         exclude=('last_date','status','notification','pay','user',)
#
#
class onlinepaymentform(forms.ModelForm):
    exp_date= forms.DateField(widget=DateInput)
    class Meta:
        model=OnlinePayment
        fields='__all__'

class schatform(forms.ModelForm):
    class Meta:
        model=Schat
        exclude=('user',)

class pchatform(forms.ModelForm):
    class Meta:
        model=Pchat
        exclude=('user',)