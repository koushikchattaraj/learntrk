from django.contrib import admin
from django.urls import path,include
from .views import about, contact, home, logout_view, signin, my_account, signup, teachers

urlpatterns = [
    path('',home,name='Home'),
    path('about/',about,name='About'),
    path('my_account/',my_account,name='my_account'),
    path('teachers/',teachers,name='teachers'),
    path('sign_in/',signin,name='sign_in'),
    path('sign_up/',signup,name='sign_up'),
    path('contact/',contact,name='contact'),
    path('logout/',logout_view,name='logout_view')
    

]


