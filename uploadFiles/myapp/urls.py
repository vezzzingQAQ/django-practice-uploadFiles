from django.urls import path
from django.urls.conf import include
from myapp import views
urlpatterns = [
    path("",views.index,name="index"),
    #users信息操作
    path("users",views.indexUsers,name="indexusers"),

    #分页
    path("usersPaged/<int:pIndex>",views.indexUsersPaged,name="userspaged"),

    path("users/add",views.addUsers,name="addusers"),
    path("users/insert",views.insertUsers,name="insertusers"),
    path("users/addRandom",views.insertRandomUsers,name="addrandomusers"),
    path("users/del/<int:userId>",views.delUsers,name="delusers"),
    path("users/edit/<int:userId>",views.editUsers,name="editusers"),
    path("users/update",views.updateUsers,name="updateusers"),

    #upload
    path("upload",views.uploadPage,name="uploadpage"),
    path("doUpload",views.doUpload,name="doupload"),

]
