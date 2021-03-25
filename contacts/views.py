from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail

def contact(request):
    if request.method == "POST":
        course_id = request.POST['course_id']
        course = request.POST['course']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']

        # Check if user has made enquiry already
        if request.user.is_authenticated :
            user_id = request.user.id
            print('user_id',user_id)
            has_contacted = Contact.objects.all().filter(course_id=course_id, user_id=user_id)
            if has_contacted:
                messages.error(request,'You have already contacted for this course')
                return redirect('/courses/'+course_id)


        
        contact = Contact(course=course, course_id=course_id, name=name, email=email,
        phone=phone, message=message, user_id=user_id)

        contact.save()

        #Send Email
        send_mail(
            'Course Inquiry',
            'There has been an inqury for ' + course + 'Sign in admin panel for more details',
            'djangoproject.testmail@gmail.com',
            ['kgattamaneni@gmail.com'],
            fail_silently=False


        )
        messages.success(request,'Your request has been submitted, We will get back to you soon')
        return redirect('/courses/'+course_id)