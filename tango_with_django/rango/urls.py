from rango import views
from django.urls import path

app_name = 'rango'

urlpatterns = [
	path('', views.index, name = 'index'),
	path('login', views.user_login, name = 'login'),
	path('logout', views.user_logout, name = 'logout'),
	path('register', views.register, name = 'register'),
	path('about', views.about, name = 'about'),
	path('category/<str:category_name_url>', views.show_category, name = 'category'),
	path('add_category', views.add_category, name = 'add_category'),
	path('category/<str:category_name_url>/add_page', views.add_page, name = 'add_page')
]