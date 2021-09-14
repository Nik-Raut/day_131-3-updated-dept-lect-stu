from django.urls import path
from .views import registraionview,loginview,logoutview

urlpatterns=[
    path('reg/',registraionview,name='reg'),
    path('login/',loginview,name='login'),
    path('logout/',logoutview,name='logout'),

]