from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Banner)
class BannerModelAdmin(admin.ModelAdmin):
    list_display= ('id','banner')