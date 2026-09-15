from django.contrib import admin

# Register your models here.
from myapp.models import Info, Course, Students

admin.site.register(Info)
admin.site.register(Course)
admin.site.register(Students)
