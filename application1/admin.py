from django.contrib import admin
from .models import Modelclass
# Register your models here.
class Adminclass(admin.ModelAdmin):
    list_display=['first_name','last_name','user_name','password','conform_password','email_id','mobile_no','gender','nationality','created_date']
admin.site.register(Modelclass,Adminclass)
