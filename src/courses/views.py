from django.shortcuts import render
# Create your views here.
from .models import Course

def course_list(request):
    courses = Course.objects.all()
    output = ' '.join([course for course in courses])
    return render(request, 'pages/index.html', context={'object': output})

