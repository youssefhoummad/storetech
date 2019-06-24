from django.contrib import admin

from .models import Device, Category, Brand, Purchase

# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Device)
admin.site.register(Purchase)
