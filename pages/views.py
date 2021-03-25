from django.shortcuts import render
from django.http import HttpResponse

from courses.models import Course
from instructors.models import Instructor
from courses.choices import course_choices, course_type_choice

def index(request):
    courses = Course.objects.order_by('-next_batch_start_date').filter(is_published=True)[:3]

    context = {
        'courses': courses,
        'course_choices' : course_choices,
        'course_type_choice' : course_type_choice
    }
    return render(request, 'pages/index.html',context)

def about(request):
    # Get all instructors
    instructors = Instructor.objects.all()
    # Get MVP
    mvp_course = Course.objects.all().filter(is_mvp=True)

    context = {
        'instructors' : instructors,
        'mvp_course' : mvp_course
    }
    return render(request, 'pages/about.html', context)

