from django.shortcuts import render
from pages.models import Team
from cars.models import Car
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    teams = Team.objects.all()
    cars = Car.objects.order_by('-created_date').all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured = True)
    data = {
        'teams': teams,
        'cars': cars,
        'featured_cars': featured_cars,
    }
    return render(request, 'pages/home.html', data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):

    if request.method == 'POST':
        user_id = request.POST['user_id']
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            name+' Contacted CarZone Regarding: '+subject,
            message+'\n\nBy: '+name+'\nEmail: '+email+'\nContact: '+phone,
            'agamseth281999@gmail.com',
            [admin_email],
            fail_silently=False,
        )
        messages.success(request, 'Your email is received successfully, we will get back to you soon.')

    return render(request, 'pages/contact.html')
