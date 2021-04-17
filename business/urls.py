from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="Homepage"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('handlesignup/', views.handleSignUp, name="handleSignUp"),
    path('handlelogin/', views.handleLogin, name="handleLogin"),
    path('handlelogout/', views.handleLogout, name="handleLogout"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path('handleoffer/', views.handleoffer, name="handleoffer"),
    path("manage/",views.manage,name="manage"),
    path("delete/<str:name>",views.delete,name="delete"),
    path('trending/', views.trending, name='trending'),
    path('search/', views.search, name='search'),
]