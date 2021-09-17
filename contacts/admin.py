from django.contrib import admin
from .models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):

    list_display = ('user_id', 'first_name', 'car_title', 'customer_need', 'email', 'city', 'create_date')
    list_display_links = ('user_id', 'car_title', 'first_name')

    search_fields = ('first_name', 'car_title', 'city')
    list_filter = ('car_title', 'city', 'email')


admin.site.register(Contact, ContactAdmin)
