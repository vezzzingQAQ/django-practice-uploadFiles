from django.shortcuts import render
from django.http import HttpResponse

from myapp.models import Users

import time,os
import random

from PIL import Image

from django.core.paginator import Paginator
# Create your views here.
def index(request):
    return(render(request,"myapp/mainPage.html"))
#浏览用户信息
def indexUsers(request):
    try:
        ulist=Users.objects.all()
        uploadContext={"userslist":ulist}
        return(render(request,"myapp/users/index.html",uploadContext))#加载模板
    except:
        return(HttpResponse("没有找到用户信息(○´･д･)ﾉ"))

#Paginator分页浏览信息
#*************************************************************************
'''
def indexUsersPaged(request,pIndex=1):
    try:
        ulist=Users.objects.filter()
        p=Paginator(ulist,15)#15条数据一页
        #判断页码值是否有效
        if pIndex<1:
            pIndex=1
        if pIndex>p.num_pages:
            pIndex=p.num_pages
        #重新返回表格
        currentlist=p.page(pIndex)
        uploadContext={"userslist":currentlist,"currentPage":pIndex,"pagesList":p.page_range}
        return(render(request,"myapp/users/indexPaged.html",uploadContext))#加载模板
    except:
        return(HttpResponse("出错啦(○´･д･)ﾉ"))
'''
#*************************************************************************
#支持查找
def indexUsersPaged(request,pIndex=1):
    try:
        #查找
        kw=request.GET.get("keyWord",None)

        mypara=""#用于储存搜索条件

        if kw is not None:
            ulist=Users.objects.filter(name__contains=kw)#模糊查询name字段
            mypara="?keyWord=%s"%(kw)
        else:
            ulist=Users.objects.filter()
        
        p=Paginator(ulist,15)#15条数据一页
        #判断页码值是否有效
        if pIndex<1:
            pIndex=1
        if pIndex>p.num_pages:
            pIndex=p.num_pages
        #重新返回表格
        currentlist=p.page(pIndex)
        uploadContext={"userslist":currentlist,"currentPage":pIndex,"pagesList":p.page_range,"mypara":mypara}
        return(render(request,"myapp/users/indexPaged.html",uploadContext))#加载模板
    except:
        return(HttpResponse("出错啦(○´･д･)ﾉ"))
#*************************************************************************

#加载添加用户信息表单
def addUsers(request):
    return(render(request,"myapp/users/add.html"))

#执行用户信息添加
#<form action="{% url 'insertusers' %}" method="POST">
def insertUsers(request):
    try:
        ob=Users()
        #从表单获取要添加的信息
        ob.name=request.POST['name']#<input name='name'...>
        ob.age=request.POST['age']
        ob.phoneNumber=request.POST['phone']
        ob.idNumber=request.POST['idnumber']
        ob.save()
        uploadContext={"info":"添加成功"}
    except:
        uploadContext={"info":"添加失败"}
    return(render(request,"myapp/users/info.html",uploadContext))

def insertRandomUsers(request):
    try:
        namePool="陈李王可心甜平雷傲宇杨"
        for i in range(10):
            ob=Users()

            tempName=""
            for j in range(3):
                tempName+=namePool[random.randrange(len(namePool))]
            ob.name=tempName

            ob.age=str(int(random.randrange(1,30)))

            tempPhoneNumber=""
            for j in range(7):
                tempPhoneNumber+=str(int(random.randrange(0,9)))
            ob.phoneNumber=tempPhoneNumber

            tempIdNumber=""
            for j in range(7):
                tempIdNumber+=str(int(random.randrange(0,9)))
            ob.idNumber=tempIdNumber

            ob.save()
        uploadContext={"info":"添加成功"}
    except:
        uploadContext={"info":"添加失败"}
    return(render(request,"myapp/users/info.html",uploadContext))
#执行用户信息删除
def delUsers(request,userId=0):
    try:
        ob=Users.objects.get(id=userId)
        ob.delete()
        uploadContext={"info":"删除成功"}
    except:
        uploadContext={"info":"删除失败"}
    return(render(request,"myapp/users/info.html",uploadContext))

#加载用户信息修改表单
def editUsers(request,userId=0):
    try:
        ob=Users.objects.get(id=userId)
        uploadContext={"user":ob}
        #<input name="id" type="hidden" value={{user.id}}>
        return(render(request,"myapp/users/edit.html",uploadContext))
    except:
        uploadContext={"info":"没有找到要修改的数据"}
        return(render(request,"myapp/users/info.html",uploadContext))

#执行用户信息修改
#<form action="{% url 'updateusers' %}" method="POST">
def updateUsers(request):
    try:
        currentid=request.POST['id']
        ob=Users.objects.get(id=currentid)
        #从表单获取要修改的信息
        ob.name=request.POST['name']
        ob.age=request.POST['age']
        ob.idNumber=request.POST['idnumber']
        ob.phoneNumber=request.POST['phone']
        ob.save()
        uploadContext={"info":"修改成功"}
    except:
        uploadContext={"info":"修改失败"}
    return(render(request,"myapp/users/info.html",uploadContext))

#*************************************************************************

def uploadPage(request):
    return(render(request,"myapp/uploadFiles/upload.html"))
'''
def doUpload(request):
    #处理上传的文件
    myfile=request.FILES.get("pic",None)
    
    if not myfile:
        return(HttpResponse("没有上传的文件信息"))
    
    print(myfile)
    print(request.POST["title"])

    #destination=open("./static/pics/a.png","wb+")#目标文件
    #生成上传后的文件名
    filename=str(time.time())+"."+myfile.name.split(".").pop()#随机时间戳+原来的后缀名
    destination=open("static/pics/"+filename,"wb+")

    for chunk in myfile.chunks():#分块读取上传文件内容并写入目标文件
        destination.write(chunk)
    destination.close()

    #用Pillow实现图片自动缩放成75*75,也可以用来加水印
    im=Image.open("static/pics/"+filename)
    im.thumbnail((75,75))
    im.save("static/pic_sized/"+filename,None)

    #os.remove(...+filename)删除原图

    return(HttpResponse("上传成功:"+filename))
'''
def doUpload(request):
    #处理上传的文件
    myfile=request.FILES.get("pic",None)
    
    if not myfile:
        return(HttpResponse("没有上传的文件信息"))
    
    print(myfile)
    print(request.POST["title"])

    #destination=open("./static/pics/a.png","wb+")#目标文件
    #生成上传后的文件名
    filename="bc"+"."+myfile.name.split(".").pop()#随机时间戳+原来的后缀名
    destination=open("static/pics/"+filename,"wb+")

    for chunk in myfile.chunks():#分块读取上传文件内容并写入目标文件
        destination.write(chunk)
    destination.close()

    #用Pillow实现图片自动缩放成75*75,也可以用来加水印
    im=Image.open("static/pics/"+filename)
    im.thumbnail((275,275))
    im.save("static/pic_sized/"+filename,None)

    #os.remove(...+filename)删除原图

    return(HttpResponse("上传成功:"+filename))

