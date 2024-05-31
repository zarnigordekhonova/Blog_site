from django.contrib import admin
from .models import Users
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id',]


admin.site.register(Users)