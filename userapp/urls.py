from django.contrib.auth import login
from django.urls import path
from . import views
from .views import *

urlpatterns=[
    path("",views.allindians,name='home'),
    path('login/', login, name='login'),
    path('login1/', login1, name='login1'),
    path('register/', Register, name='register'),
    path('sign/', signup1, name='signup1'),
    path('logout/', logout, name='logout'),
    path('item/<str:title>/<str:category>/', views.item, name='item'),
    path('map/', map, name='maps'),
    path('contact/', contact, name='contact'),
path('add/',addindian, name='adddata'),

]