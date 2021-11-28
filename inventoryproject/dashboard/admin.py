from django.contrib import admin
from .models import Product, Order
# from django.contrib.auth.models import Group

# change the admin site header
admin.site.site_header = 'Depo Sistemi Admin Sayfası'

# set the columns that will be displayed on products admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity')
    # adds filter functionality
    list_filter = ['category']

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
# to unregister Groups on admin site
# admin.site.unregister(Group)
