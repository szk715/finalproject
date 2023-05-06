"""server_bak URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from user import views
from images import views as images
from weapon import views as weapon
from match import views as match
from myweapon import views as myweapon
from matchuser import views as matchuser
from scene import views as scene
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/info',views.info,name='info'),
    path('user/delete',views.delete,name='delete'),
    path('user/list',views.list,name='list'),
    path('user/login',views.login,name='login'),#登录
    path('user/registry',views.save,name='registry'),#登录
    path('user/page',views.page,name='pag'),#登录
    path('user/update',views.update,name='update'),#登录
    path('images/info',images.info,name='info'),#详情
    path('images/delete',images.delete,name='delete'),#删除
    path('images/list',images.list,name='list'),#查询所有
    path('images/save',images.save,name='save'),#新增
    path('images/update',images.update,name='update'),#修改
    path('images/page',images.page,name='pag'),#分页页查询
    path('images/upload',images.upload,name='upload'),#文件上传
    path('weapon/info',weapon.info,name='info'),#详情
    path('weapon/delete',weapon.delete,name='delete'),#删除
    path('weapon/list',weapon.list,name='list'),#查询所有
    path('weapon/save',weapon.save,name='save'),#新增
    path('weapon/update',weapon.update,name='update'),#修改
    path('weapon/page',weapon.page,name='pag'),#分页条件查询
    path('match/info',match.info,name='info'),#详情
    path('match/delete',match.delete,name='delete'),#删除
    path('match/list',match.list,name='list'),#查询所有
    path('match/save',match.save,name='save'),#新增
    path('match/update',match.update,name='update'),#修改
    path('match/page',match.page,name='pag'),#分页条件查询
    path('myweapon/info',myweapon.info,name='info'),#详情
    path('myweapon/fire',myweapon.fire,name='fire'),#武器攻击
    path('myweapon/defense',myweapon.defense,name='defense'),#武器攻击
    path('myweapon/delete',myweapon.delete,name='delete'),#删除
    path('myweapon/list',myweapon.list,name='list'),#查询所有
    path('myweapon/save',myweapon.save,name='save'),#新增
    path('myweapon/update',myweapon.update,name='update'),#修改
    path('myweapon/page',myweapon.page,name='pag'),#分页条件查询
    path('matchuser/info',matchuser.info,name='info'),#详情
    path('matchuser/delete',matchuser.delete,name='delete'),#删除
    path('matchuser/list',matchuser.list,name='list'),#查询所有
    path('matchuser/save',matchuser.save,name='save'),#新增
    path('matchuser/update',matchuser.update,name='update'),#修改
    path('matchuser/page',matchuser.page,name='pag'),#分页条件查询
    path('scene/info',scene.info,name='info'),#详情
    path('scene/delete',scene.delete,name='delete'),#删除
    path('scene/list',scene.list,name='list'),#查询所有
    path('scene/save',scene.save,name='save'),#新增
    path('scene/update',scene.update,name='update'),#修改
    path('scene/page',scene.page,name='pag'),#分页条件查询

]

#urlpatterns += [url('silk/', include('silk.urls', namespace='silk'))]
