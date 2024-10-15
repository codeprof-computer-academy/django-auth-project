from django.urls import path
from . import views

urlpatterns = [

      path('', views.homePage, name="home"),
      path('register/', views.registerPage, name="register"),
      path('login/', views.loginPage, name="login"),
      path('dashboard/', views.dashboard, name="dashboard"),

]
