from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
"""class Wxuser(models.Model):
    id = models.AutoField(primary_key=True)
    openid=models.CharField(max_length=255)
    name = models.CharField(max_length=50)
    avatar = models.CharField(max_length=200)
    language = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    #gender = models.CharField(max_length=50)
    creat_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.openid
"""


class Porders(models.Model):
    porder_id = models.AutoField(primary_key=True)
    P_gender = models.CharField(max_length=10)
    P_userid = models.CharField(max_length=100)
    P_sport = models.IntegerField(blank=False,null=False)
    P_number = models.IntegerField(blank=False,null=False)
    P_level = models.IntegerField(blank=False,null=False)
    P_pgender = models.IntegerField(blank=False,null=False)
    P_times = models.TimeField(blank=False,null=False)
    P_date = models.DateField(blank=False,null=False)
    P_createdatetime = models.DateTimeField(auto_now=True)
    P_latitudes = models.FloatField(blank=False,null=False)
    P_longitudes = models.FloatField(blank=False,null=False)
    P_address = models.CharField(max_length=100,blank=False,null=False)
    P_hasnum = models.IntegerField(blank=False, null=False)
    P_suc = models.BooleanField(default=False)
    class Meta:
        ordering = ('porder_id',)
    def __str__(self):
        return self.P_userid


"""class Cporder(models.Model):
    cporder_id = porder_id = models.AutoField(primary_key=True)
    porder_id 
    P_opid = models.CharField(mx)
    Cp_createdatetime = models.DateTimeField(auto_now=True)"""
class Pcontent(models.Model):
    content_id = models.AutoField(primary_key=True)
    Porder_id = models.CharField(max_length=10)
    P_username = models.CharField(max_length=30)
    P_userid = models.CharField(max_length=100)
    C_content = models.CharField(max_length=30)
    C_createdatetime = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('content_id',)
    def __str__(self):
        return self.content_id

class Puorder(models.Model):
    Puorder_id = models.AutoField(primary_key=True)
    porder_id = models.CharField(max_length=1000)
    P_userid = models.CharField(max_length=100)
    P_createdatetime = models.DateTimeField(auto_now=True)

class userrecord(models.Model):
    userid = models.CharField(max_length=100)
    ordernum = models.IntegerField(blank=False,null=False,default=0)
    height = models.CharField(max_length=5,default=0)
    weight = models.CharField(max_length=5,default=0)
    age = models.CharField(max_length=5,default=0)