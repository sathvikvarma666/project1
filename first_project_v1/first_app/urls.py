from django.contrib import admin
from django.urls import path
from first_app import views
from django.urls import re_path

app_name = 'first_app'

urlpatterns = [
    re_path(r'^$',views.base,name="base"),
    re_path(r'^/other',views.other,name="other"),
    re_path(r'^/relative',views.relative,name="relative"),
    re_path(r'^/register',views.register,name="register")

    # path('/help',views.help),

]