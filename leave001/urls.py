from django.conf.urls import url
from . import views
from django.contrib.auth import views as view


urlpatterns=[
    url(r'^$',views.home),
    url(r'^accounts/login/apply/',views.apply,name="apply"),
    url(r'^accounts/login/', view.login, name='login'),
    url(r'^signup/',views.signup,name='signup'),
    url(r'^applied/',views.applied,name='data')]