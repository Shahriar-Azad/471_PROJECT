"""
URL configuration for tutor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from system.views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('register',register,name='register'),
    path('t_login',t_login,name='t_login'),
    path('t_home',t_home,name="t_home"),
    path('contact',contact,name="contact"),
    path('visa',payment,name="visa"),
    path('bkash',bkash,name="bkash"),
    path('nagad',nagad,name="nagad"),
    path('reset_password', auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name="reset_password"),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),name="password_reset_confirm"),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),name="password_reset_complete"),
    path('video',video,name="video"),
    path('available',available,name="available"),
   # path('export-to-excel/', export_to_excel, name='export_to_excel'),
    path('tutor_reg',tutor_reg,name='tutor_reg'),
    path('tutor_reg2',tutor_reg2,name='tutor_reg2'),
    path('profile',profile,name='profile'),
    path('Addtutor',addtutor1,name='Addtutor'),
    path('notification',notification,name='notification'),
    path('nonotification',notification,name='nonotification'),
    path('home',home,name="home"),
    path('<str:room>/',room,name='room'),
    path('checkview',checkview,name="checkview"),
    path('send',send,name="send"),
    path('getMessages/<str:room>/',getMessages,name='getMessages'),
    path('edurecors',t_home,name="edurecors"),
    path('ratings',ratings,name='ratings'),
]
