from django.contrib import admin
# Register your models here.
from .models import Porders,Pcontent,Puorder,userrecord

class PorderAdmin(admin.ModelAdmin):
    list_display = ('porder_id','P_hasnum','P_gender', 'P_userid', 'P_sport', 'P_number', 'P_level', 'P_pgender', 'P_address','P_latitudes','P_longitudes','P_times' ,'P_date', 'P_createdatetime','P_suc')

class ContentAdmin(admin.ModelAdmin):
    list_display = ('content_id','Porder_id','P_username','P_userid','C_content','C_createdatetime')

class PuorderAdmin(admin.ModelAdmin):
    list_display = ('Puorder_id','porder_id','P_userid','P_createdatetime')

class userrecordrAdmin(admin.ModelAdmin):
    list_display = ('userid','ordernum','height','weight','age')
admin.site.register(Porders,PorderAdmin)
admin.site.register(Pcontent,ContentAdmin)
admin.site.register(Puorder,PuorderAdmin)
admin.site.register(userrecord,userrecordrAdmin)