from django.shortcuts import render, get_object_or_404
from .models import Course
from django.core.paginator import Paginator, EmptyPage
from courses.choices import course_type_choice, course_choices


def index(request):
    courses = Course.objects.order_by('-next_batch_start_date').filter(is_published=True)

    paginator = Paginator(courses, 6)
    page = request.GET.get('page')
    paged_courses = paginator.get_page(page)

    context = {
        'courses': paged_courses

    }

    return render(request, 'courses/courses.html', context)

def course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    context = {
        'course' : course,
    }
    return render(request, 'courses/course.html', context)

def search(request):
    queryset_list = Course.objects.order_by('-title')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # Course
    if 'course' in request.GET:
        course = request.GET['course']
        if course:
            queryset_list = queryset_list.filter(title__icontains=course)

    # Course Mode
    if 'course_mode' in request.GET:
        course_mode = request.GET['course_mode']
        if course_mode :
            queryset_list =  queryset_list.filter(course_mode__icontains=course_mode)
            

    context = {
        'course_choices' : course_choices,
        'course_type_choice' : course_type_choice,
        'courses' : queryset_list,
        'values' : request.GET
    }
    return render(request, 'courses/search.html', context)