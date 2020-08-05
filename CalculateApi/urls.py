from django.conf.urls import url
from . import views

urlpatterns = [
    url('findorder', views.find_order),
    url('upset',views.get_order),
    url('getopenid',views.userInfo),
    url('getcontent',views.get_content),
    url('content',views.find_content),
    url('findsucorder',views.find_sucorder),
    url('deleteorder',views.delete_order),
    url('getuinfo',views.getuinfo),
    url('cuinfo',views.personinfo),
]