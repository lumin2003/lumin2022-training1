from django.shortcuts import redirect
from django.shortcuts import render
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_protect

from calculate.jisuan import jisuan
from hello import models
from hello.models import UserInfo


# Create your views here.


def calculate(request):
    return render(request, 'counter.html')


def show(request):
    x = request.POST.get('x')
    y = request.POST.get('y')
    result = jisuan(x,y)
    return render(request, 'result.html', {'result':result})


def lists(req):
    data = {}
    listdata = models.UserInfo.objects.all()
    data['list'] = listdata
    return render(req, 'lists.html', data)


# 路由中指定要调用的函数,传入一个用户请求参数
import MySQLdb #2


def index(request):
    # 返回HTML页面时,使用render来渲染和打包
#2
    data = {}
    listdata = UserInfo.objects.all()
    data['index'] = listdata
    return render(request, 'index.html', data)


def insert(request):
    if request.method == 'GET':
       return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST.get("username", None) # change from get("username") to get("name")
        password = request.POST.get("password", None)
        mail = request.POST.get("email", None)
        age = request.POST.get("age", None)
        address = request.POST.get("address", None)
        tem=UserInfo.objects.create(username=username, password=password, email=mail, age=age, address=address,
                                       create_date=now()) #change model.UserInfo to UserInfo
        return redirect('/index/')


def edit(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        conn = MySQLdb.connect(host="localhost", user="root", passwd="123456Zlm!!", db="lumin_form", charset='utf8')
        with conn.cursor() as cursor:
            cursor.execute("SELECT id,username,password,address,create_date,email FROM hello_UserInfo where id =%s", [id])
            UsersInfo = cursor.fetchone()
        return render(request, 'edit.html', {'UsersInfo': UsersInfo})
    else:
        id = request.POST.get("id")
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        address = request.POST.get('address', '')
        create_date = request.POST.get('create_date', '')
        email = request.POST.get('email', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="123456Zlm!!", db="lumin_form", charset='utf8')
        with conn.cursor() as cursor:
            cursor.execute("UPDATE hello_UserInfo set username=%s,password=%s,address=%s,create_date=%s,email=%s where id =%s", [username,password,address,create_date,email, id])
    conn.commit()
    return redirect('edit.html')
# 学生信息删除处理函数，同上，SQL语句改变而已。




#2 学生信息删除处理函数，同上，SQL语句改变而已。
def delete_user(request, UserInfo_id):
    UserInfo = get_object_or_404(UserInfo, pk=UserInfo_id)
    if request.method == 'POST':
        UserInfo.delete()
        return redirect('/index/')
    return render(request, 'index.html', {'UserInfo': UserInfo})


from django.http import HttpResponseRedirect, Http404
from tablib import Dataset
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from hello.resources import UserInfoResource
import io
from io import StringIO
import csv
from csv import reader
from .models import UserInfo
from django.urls import reverse
import logging


def upload(request):
    if request.method == 'POST':
        UserInfo_resource = UserInfoResource()
        # dataset = UserInfo_resource.export()
        new_UserInfo = request.FILES['myfile']
        tem2 = new_UserInfo.read().decode('utf-8')
        rows = []
        lines = tem2.split('\n')
        created = None
        created_records = 0

        for line in lines:
            fields = line.split(",")
            print("line",line)
            data_dict = {}

            class data_dict:
                def __init__(self, username, password, address, create_date, email):
                    self.username = username
                    self.password = password
                    self.address = address
                    self.create_date = create_date
                    self.email = email

            data_dict.username = fields[0]
            data_dict.password = fields[1]
            print("fields[1]", fields[1])
            data_dict.address = fields[2]
            data_dict.create_date = fields[3]
            data_dict.email = fields[4]

        if created:
            created_records += 1
        result = UserInfo_resource.import_data(tem2, dry_run=True)
        return redirect('/index/')