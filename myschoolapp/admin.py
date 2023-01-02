from django.contrib import admin

# Register your models here.
from myschoolapp import models

admin.site.register(models.Course)
