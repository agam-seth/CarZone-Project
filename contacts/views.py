from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.

def inquiry(request):

    if request.method == 'POST':

        user_id = request.POST['user_id']
        car_id =request.POST['car_id']
        price = request.POST['price']

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        car_title = request.POST['car_title']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if Contact.objects.filter(user_id=user_id, car_id=car_id, customer_need=customer_need).exists():
            messages.error(request, 'This request already exist, we will get back to you as soon as possible.')
            return redirect('/cars/'+car_id)
        else:
            contact = Contact(user_id=user_id, car_id=car_id, price=price, first_name=first_name,
                                last_name=last_name, customer_need=customer_need, car_title=car_title,
                                city=city, state=state, email=email, phone=phone, message=message)

            admin_info = User.objects.get(is_superuser=True)
            admin_email = admin_info.email
            send_mail(
                'Inquiry Regarding ' + car_title,
                'You have a new inquiry regarding car: '+car_title+' by '+first_name+' '+last_name+'. He/She said, "'+customer_need+'". Please login to Admin Panel for more details.',
                'agamseth281999@gmail.com',
                [admin_email],
                fail_silently=False,
            )

            contact.save()
            messages.success(request, 'Your request has been submitted, we will get back to you soon.')
            return redirect('/cars/'+car_id)
