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
        email = request.POST.get("email", None)
        age = request.POST.get("age", None)
        address = request.POST.get("address", None)
        sex = request.POST.get("sex", None)
        UserInfo.objects.create(username=username, address=address, password=password,  age=age,
                                       create_date=now(), email=email,sex=sex) #change model.UserInfo to UserInfo
        return redirect('/index/')


def edit_user(request):
    edit_id = request.GET.get('id')
    if request.method == 'POST':
        new_pwd = request.POST.get('password')
        new_address = request.POST.get('address')
        new_age = request.POST.get('age')
        new_email = request.POST.get('email')
        new_sex = request.POST.get('sex')

        edit_obj = models.UserInfo.objects.get(id=edit_id)
        edit_obj.password = new_pwd
        edit_obj.address = new_address
        edit_obj.age = new_age
        edit_obj.email = new_email
        edit_obj.sex = new_sex
        # 保存数据库
        edit_obj.save()
        return redirect('/index/')
    ret = models.UserInfo.objects.get(id=edit_id)
    return render(request, 'edit.html', {'ret': ret})

def add_user(request):
    error_name = ''
    if request.method == 'POST':
    # 1、获取前端输入的数据
        user = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        age = request.POST.get('age')
        email = request.POST.get('email')
        sex = request.POST.get('sex')
        user_list = models.UserInfo.objects.filter(username=user)
         # 2、判断数据库是否存在
        if user_list :
                error_name = '%s用户名已经存在了' % user
                return  render(request,'add_user.html',{'error_name':error_name})
        # 3、存储到数据库中
        else:
            tem = models.UserInfo.objects.create(username=user,
                                       password=password,
                                       address=address,
                                       age=age,
                                       create_date=now(),
                                       email=email,
                                       sex=sex)
            user.save()
            return redirect('/index/')
    return render(request, 'add_user.html')



#2 学生信息删除处理函数，同上，SQL语句改变而已。
def delete_user(request):
    delete_id = request.GET.get('id')
    # 从数据库删除的
    models.UserInfo.objects.filter(id=delete_id).delete()
    return redirect('/index/')
    #return render(request, 'index.html', {'UserInfo': UserInfo})


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
import pandas as pd


def csv_upload(request):
    print("i am here4")
    template = "index.html"
    data = UserInfo.objects.all()
    print("i am here3")
    prompt = {
        'order': 'Order of the CSV should be username, password, address,age, sex',
        'UserInfo': data
    }
    print("i am here2")
    if request.method == 'POST':
        new_UserInfo = request.FILES['myfile']
        print("i am here6")
    tem2 = new_UserInfo.read().decode('utf-8')
    print("i am here")
    io_string = io.StringIO(tem2)
    print("io_string",io_string)
    #next(io_string) #removal header
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
           _, created = UserInfo.objects.update_or_create (
               username=column[0],
               password=column[1],
               address=column[2],
               age = column[3],
               create_date = column[4],
               email=column[5],
               sex=column[6]
               )
           context = dict()
    print("context",context)
    return redirect('/index',context)