from django.contrib import admin
from cars.models import Car
from django.utils.html import format_html

# Register your models here.

class CarAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html('<img src="{}" width="50" style="border-radius:50%;"/>'.format(object.car_photo.url))

    thumbnail.short_description = 'Car Image'

    list_display = ('id', 'thumbnail', 'title', 'body_style', 'condition', 'price', 'is_featured', 'created_date',)
    list_display_links = ('id', 'thumbnail', 'title',)

    search_fields = ('title', 'condition', 'body_style', 'city',)
    list_filter = ('condition', 'body_style', 'fule_type',)

    list_editable = ('is_featured', )

admin.site.register(Car, CarAdmin)
