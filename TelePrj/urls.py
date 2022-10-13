"""TelePrj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from App import views

from django.urls import include, path
from rest_framework import routers
from App.viewsets import prepaidViewSet,postpaidsiewSet
from django.contrib import admin
from django.urls import path


router = routers.DefaultRouter()
router.register(
    'list',prepaidViewSet, basename='list',

)
router.register(
    'list1',postpaidsiewSet, basename='list1',

)

urlpatterns = [
    path('chat',views.mainpage.as_view(),),
    path('admin/', admin.site.urls),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('adlogin/',views.adlogin,name="adlogin"),
    path('logout/',views.logout,name="logout"),
    path('home',views.home,name="home"),
    path('home1/', views.home1, name="home1"),
    path('api/', include(router.urls)),
    path('show',views.show,name='show'),
    path('success', views.success, name='success'),
    path('simpurchase',views.show1,name='show1'),
path('Postpaidbuysim',views.show3,name='show3'),
    path('new',views.new,name='new'),
    path('mobilenumbergeneration',views.mobilenumbergeneration,name='mobilenumbergeneration'),
    path('Paid',views.Paid,name='Paid'),
    path('Payment',views.Payment,name='Payment'),
    path('add5',views.add5,name='add5'),
    path('postpaidmobilenumbergeneration', views.postpaidmobilenumbergeneration, name='postpaidmobilenumbergeneration'),
    path('buy/',views.buy,name='buy'),
    path('buy1/',views.buy1,name='buy1'),
    path('buy2/',views.buy2,name='buy2'),
    path('buy3/',views.buy3,name='buy3'),
    path('prepaidrecharge/<pp>',views.new1,name='new1'),
    #path('profilenew1',views.profilenew1,name='profilenew1'),
    path('postpaidbillpayment',views.postpaidbillpayment,name='postpaidbillpayment'),
    path('myprofile', views.myprofile, name='myprofile'),
    path('new2',views.new2,name='new2'),
    path('new3',views.new3,name='new3'),
    path('new4',views.new4,name='new4'),
    path('Billpayment',views.new5,name='new5'),
    path('new6', views.new6, name='new6'),
    path('credit',views.fun),
    path('check',views.myprofile),
    path('check1',views.postpaidbillpayment),
   path('credit3',views.credit3,name='credit3'),
path('credit2',views.credit2,name='credit2'),
    path('credit1/<id1>',views.credit1,name='credit1'),
path('credit4',views.fun1),
path('credit5',views.credit5,name='credit5'),
path('credit6',views.credit6,name='credit6'),
path('credit7',views.myprofile,name='credit7'),
path('credit9',views.myprofile,name='credit9'),
path('credit8',views.myprofile,name='credit8'),
path('credit10',views.postpaidbillpayment,name='credit10'),
path('credit12',views.postpaidbillpayment,name='credit12'),
    path('update/<id>', views.update, name="update"),
    path('delete/<id>', views.delete, name="delete"),
    path('prepaid', views.prepaidd, name="prepaid"),
    path('postpaid', views.postpaidd, name="postpaid"),
    path('feedback',views.RenderFeed1),
    path('AddFeed',views.AddFeed),
    path('showfeed',views.ShowFeed),
    path('about',views.about,name='about'),
    path('queries', views.RenderFeed),
    path('newqueries', views.AddFeed1)
]

