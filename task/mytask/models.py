from django.db import models

# Create your models here.
class Data(models.Model):  
    email = models.EmailField(max_length=30, unique=True)
    password = models.CharField(max_length=8)
    status = models.IntegerField()  
    class Meta:  
        db_table = "userdata"  