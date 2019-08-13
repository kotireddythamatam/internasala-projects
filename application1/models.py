from django.db import models

class Modelclass(models.Model):
    first_name=models.CharField(max_length=15,default='enter first name',blank=True)
    last_name=models.CharField(max_length=15,null=True)
    user_name=models.CharField(max_length=15)
    password=models.CharField(max_length=8)
    conform_password=models.CharField(max_length=8)
    email_id=models.EmailField()
    mobile_no=models.IntegerField()
    gender=models.CharField(max_length=6)
    nationality=models.CharField(max_length=10)
    created_date=models.DateTimeField(auto_now_add=True)
