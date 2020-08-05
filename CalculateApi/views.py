from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.core import serializers
import requests
from json import loads,dumps
from .models import Porders,Pcontent,Puorder,userrecord
from datetime import datetime
import heapq


def calculate(request):
    formula = request.GET['formula']
    try:
        result = eval(formula, {})
    except:
        result = 'Error formula'
    return HttpResponse(result)

def get_order(request):
    num = [0, 2, 3, 4, 5, 6, 10, 11]
    if (request.method == 'POST'):
        postBody = request.body
        json_result = loads(postBody)
    porderlist = Porders.objects.filter(P_sport=json_result['sportname'],P_level=json_result['sportlevel'],P_date=json_result['date'],P_address=json_result['address'],P_suc=False).order_by('P_createdatetime')
    if porderlist.exists():
        plist = []
        for i in list(porderlist):
            pdict = {}
            pdict['porder_id']=i.porder_id
            pdict['P_userid'] = i.P_userid
            if (i.P_gender == 'female'):
                pdict['P_gender'] = 2
            else:
                pdict['P_gender'] = 1
            pdict['P_sport'] = i.P_sport
            pdict['P_number'] = i.P_number
            pdict['P_level'] = i.P_level
            pdict['P_pgender'] = i.P_pgender
            pdict['P_times'] = i.P_times
            pdict['P_date'] = i.P_date
            pdict['P_latitudes'] = i.P_latitudes
            pdict['P_longitudes'] = i.P_longitudes
            pdict['P_hasnum'] = i.P_hasnum
            pdict['adreess'] = i.P_address
            pdict['P_suc'] = i.P_suc
            plist.append(pdict)
        takeorder = []
        for order in plist:
            cday = datetime.strptime(json_result['time'],'%H:%M')
            order['P_times'] = datetime.strptime(str(order['P_times']), '%H:%M:%S')
            if(json_result['ugender']=='female'):
                json_result['ugender'] = 2
            else:
                json_result['ugender'] = 1
            print(order)
            if(order['P_userid']!=json_result['opid']):
                print('id成功')
                if(order['P_suc'] == False):
                    if((order['P_gender']==int(json_result['ugender']) and json_result['sportgender'] == '1' and order['P_pgender']==1) or (json_result['sportgender'] == '2' and order['P_pgender']==2)):
                        print("性别匹配成功")
                        if(pdict['adreess']==json_result['address']):
                            print('地点匹配成功')
                            if( order['P_times'] - cday <datetime.strptime("00:30:00", '%H:%M:%S')-datetime.strptime("00:00:00", '%H:%M:%S') ):
                                takeorder1 = order
                                takeorder1['dtime'] = order['P_times'] - cday
                                takeorder.append(takeorder1)
                                print("时间匹配成功")
            else:
                print('ID相同')
        a = heapq.nsmallest(1,takeorder,key=lambda s: s['dtime'])
        if(len(a)==0):
            print('不存在自己创建')
            if (json_result['ugender'] == 2):
                json_result['ugender'] = "female"
            else:
                json_result['ugender'] = "male"
            Porders.objects.create(P_gender=json_result['ugender'], P_userid=json_result['opid'],
                                   P_sport=json_result['sportname'], P_number=json_result['sportnum'],
                                   P_level=json_result['sportlevel'], P_pgender=json_result['sportgender'],
                                   P_times=json_result['time'], P_date=json_result['date'],
                                   P_address=json_result['address'], P_latitudes=json_result['latitude'],
                                   P_longitudes=json_result['longitude'],P_hasnum=1)
            print('dasdsadasdasdasd')
            b = Porders.objects.filter(P_gender=json_result['ugender'], P_userid=json_result['opid'],
                                   P_sport=json_result['sportname'], P_number=json_result['sportnum'],
                                   P_level=json_result['sportlevel'], P_pgender=json_result['sportgender'],
                                   P_times=json_result['time'], P_date=json_result['date'],
                                   P_address=json_result['address'], P_latitudes=json_result['latitude'],
                                   P_longitudes=json_result['longitude'],P_hasnum=1)
            temp = list(b)
            Puorder.objects.create(porder_id=temp[0].porder_id, P_userid=json_result['opid'])
        else:
            print('添加已有')
            # 更新数据库人数添加
            if ((a[0]['P_hasnum'] + 1) == num[a[0]['P_number']]):
                print("人数已满")
                print(a[0]['P_hasnum'] + 1)
                Porders.objects.filter(porder_id=a[0]['porder_id']).update(P_hasnum=(a[0]['P_hasnum'] + 1), P_suc=True)
                usr = userrecord.objects.filter(userid=json_result['opid'])
                usr = list(usr)
                userrecord.objects.filter(userid=json_result['opid']).update(ordernum = usr[0].ordernum + 1)
            else:
                Porders.objects.filter(porder_id=a[0]['porder_id']).update(P_hasnum=a[0]['P_hasnum'] + 1)
            Puorder.objects.create(porder_id=a[0]['porder_id'], P_userid=json_result['opid'])
    else:
        print('123不存在自己创建')
        if (json_result['ugender'] == 2):
            json_result['ugender'] = "female"
        else:
            json_result['ugender'] = "male"
        Porders.objects.create(P_gender=json_result['ugender'], P_userid=json_result['opid'],
                               P_sport=json_result['sportname'], P_number=json_result['sportnum'],
                               P_level=json_result['sportlevel'], P_pgender=json_result['sportgender'],
                               P_times=json_result['time'], P_date=json_result['date'],
                               P_address=json_result['address'], P_latitudes=json_result['latitude'],
                               P_longitudes=json_result['longitude'], P_hasnum=1)
        b = Porders.objects.filter(P_gender=json_result['ugender'], P_userid=json_result['opid'],
                                   P_sport=json_result['sportname'], P_number=json_result['sportnum'],
                                   P_level=json_result['sportlevel'], P_pgender=json_result['sportgender'],
                                   P_times=json_result['time'], P_date=json_result['date'],
                                   P_address=json_result['address'], P_latitudes=json_result['latitude'],
                                   P_longitudes=json_result['longitude'], P_hasnum=1)
        temp = list(b)
        Puorder.objects.create(porder_id=temp[0].porder_id,P_userid=json_result['opid'])
        print('success')
        #Porders.objects.create(P_gender=json_result['ugender'], P_userid=json_result['opid'], P_sport=json_result['sportname'], P_number=json_result['sportnum'], P_level=json_result['sportlevel'], P_pgender=json_result['sportgender'], P_times=json_result['time'],P_date=json_result['date'],P_address=json_result['address'],P_latitudes=json_result['latitude'],P_longitudes=json_result['longitude'],P_hasnum=1)
    return HttpResponse('suceess')

def userInfo(request):
    code=request.GET['code']
    print(code)
    url = "https://api.weixin.qq.com/sns/jscode2session?appid=wx7a8ccffb2d81ae2c&secret=10b7f252f666a113f391412758c1e2e8&js_code=%s&grant_type=authorization_code" %code
    print(url)
    result = requests.get(url).content.decode("utf-8")
    result=loads(result)['openid']
    print(result)
    a = userrecord.objects.filter(userid=result)
    if(len(a)!=0):
        print("用户已经存在")
    else:
        userrecord.objects.create(userid=result)
    return HttpResponse(result)

def find_order(request):
    if (request.method == 'POST'):
        postBody = request.body
        json_result = loads(postBody)
    porderindex = Puorder.objects.filter(P_userid=json_result['openid'])
    index  = list(porderindex)
    plists = []
    for i in index:
        plists.append(int(i.porder_id))
    print(plists)
    porderlist = Porders.objects.filter(pk__in=plists,P_suc=False).order_by('P_createdatetime')
    plist = serializers.serialize("json", porderlist)
    print(plist)
    return HttpResponse(plist)

def find_sucorder(request):
    if (request.method == 'POST'):
        postBody = request.body
        json_result = loads(postBody)
    porderindex = Puorder.objects.filter(P_userid=json_result['openid'])
    index  = list(porderindex)
    plists = []
    for i in index:
        plists.append(int(i.porder_id))
    print(plists)
    porderlist = Porders.objects.filter(pk__in=plists,P_suc=True).order_by('P_createdatetime').reverse()
    plist = serializers.serialize("json", porderlist)
    print(plist)
    return HttpResponse(plist)

def find_content(request):
    if (request.method == 'POST'):
        postBody = request.body
        json_result = loads(postBody)
        print(json_result)
    porderlist = Pcontent.objects.filter(Porder_id=json_result['order_id']).order_by('content_id').reverse()
    plist = [serializers.serialize("json",porderlist)]
    print(plist)
    return HttpResponse(plist)

def delete_order(request):
    if (request.method == 'POST'):
        postBody = request.body
        json_result = loads(postBody)
        print(json_result)
    porderlist = Puorder.objects.filter(porder_id=json_result['order_id'],P_userid=json_result['openid']).delete()
    a = Porders.objects.filter(porder_id=json_result['order_id'])
    temp = list(a)
    print('1232132121321321312',temp[0].porder_id)
    if((temp[0].P_hasnum - 1 )== 0):
        print('删除了')
        Porders.objects.filter(porder_id=temp[0].porder_id).delete()
    else:
        Porders.objects.filter(porder_id=temp[0].porder_id).update(P_hasnum=(temp[0].P_hasnum - 1))
    return HttpResponse("success")

def get_content(request):
    if (request.method == 'POST'):
        postBody = request.body
        json_result = loads(postBody)
        print(json_result)
    try:
        print(123)
        Pcontent.objects.create(Porder_id=json_result["order_id"],P_username=json_result["name"],P_userid=json_result["openid"],C_content=json_result["content"])
    except:
        print('123')
    return HttpResponse('suceess')

def personinfo(request):
    if(request.method == 'POST'):
        postBody = request.body
        json_result = loads(postBody)
        print(json_result)
    try:
        userrecord.objects.filter(userid=json_result['opid']).update(height = json_result['height'],weight=json_result['weight'],age = json_result['age'])
    except:
        print('123')
    return HttpResponse('suceess')

def getuinfo(request):
    if(request.method == 'POST'):
        postBody = request.body
        json_result = loads(postBody)
        print(json_result)
    try:
        infou = userrecord.objects.filter(userid=json_result['opid'])
        print(infou)
        plist = serializers.serialize("json", infou)
        print(plist)
        return HttpResponse(plist)
    except:
        print('123')
    return HttpResponse('failed')
