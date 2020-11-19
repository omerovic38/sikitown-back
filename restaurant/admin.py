from django.contrib import admin
from restaurant.models import Restaurant, Wunschliste, Menu

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Wunschliste)
admin.site.register(Menu)
