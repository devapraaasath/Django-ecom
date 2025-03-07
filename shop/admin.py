from django.contrib import admin
from .models import *
# Register your models here.
'''
class categoryadmin(admin.ModelAdmin):
    list_display=("Name",'image','descrpiton')

admin.site.register(Catagory,categoryadmin)
'''

admin.site.register(Category)
admin.site.register(Product)