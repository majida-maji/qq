from django.contrib import admin

# Register your models here.
from myschoolapp import models

admin.site.register(models.Course)
admin.site.register(models.Notification)
admin.site.register(models.TeacherAttendance)
