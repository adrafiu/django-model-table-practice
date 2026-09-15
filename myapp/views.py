from django.shortcuts import render
from myapp.models import Info 
from myapp.models import Course
from myapp.models import Students


# Create your views here.
def home(request):
    data = Info.objects.all()
    context = {
        'data': data
    }
    return render(request, 'home.html', context) 

def course(request):
    data = Course.objects.all()
    context = {
        'data': data
    }
    return render(request, 'course.html', context)

def students(request):
    data = Students.objects.all()
    context = {
        'data': data
    }
    return render(request, 'students.html', context)


