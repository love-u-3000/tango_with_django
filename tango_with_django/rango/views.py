from django.shortcuts import render

from django.http import HttpResponse

from .models import Category, Page

def show_category(request, category_name_url):
	context_dict = {}
	try:
		cat = Category.objects.get(slug = category_name_url)
		pages = Page.objects.filter(category = cat)
		context_dict['pages'] = pages
		context_dict['category'] = cat
	except Category.DoesNotExist:
		context_dict['pages'] = None
		context_dict['category'] = None
	return render(request, 'rango/category.html', context_dict)

def index(request):
	cat = Category.objects.order_by('-likes')[:5]
	pages = Page.objects.order_by('-views')[:5]
	context_dict = {'categories': cat,
					'pages': pages}
	return render(request, 'rango/index.html', context_dict)

def about(request):
	context_dict = {'msg': 'hello dear friends'}
	return render(request, 'rango/about.html', context = context_dict)