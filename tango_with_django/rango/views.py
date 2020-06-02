from django.shortcuts import render

from django.http import HttpResponse

from .models import Category, Page

def index(request):
	cat = Category.objects.order_by('-likes')[:5]
	context_dict = {'categories': cat}
	return render(request, 'rango/index.html', context_dict)

def about(request):
	context_dict = {'msg': 'hello dear friends'}
	return render(request, 'rango/about.html', context = context_dict)