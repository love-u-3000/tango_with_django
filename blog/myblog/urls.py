
from django.urls import path, include
from myblog import views

app_name = 'myblog'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('editpost/<int:pk>', views.editpost, name = 'editpost'),
    path('register', views.register, name = 'register'),
    path('login', views.user_login, name = 'login'),
    path('logout', views.user_logout, name = 'logout'),
    path('addpost', views.addpost, name = 'addpost'),
]