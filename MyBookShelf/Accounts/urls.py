from django.urls import path
from . import views as acc_views


urlpatterns = [
    path('',acc_views.home,name='account_home'),
    path('register/',acc_views.register,name='account_register'),
    path('login/',acc_views.login,name='account_login'),
    path('logout/',acc_views.logout,name='account_logout')
]