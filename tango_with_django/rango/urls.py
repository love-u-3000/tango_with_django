from rango import views
from django.urls import path

app_name = 'rango'

urlpatterns = [
	path('', views.index, name = 'index'),
	path('about', views.about, name = 'about'),
	path('category/<str:category_name_url>', views.show_category, name = 'category')
]