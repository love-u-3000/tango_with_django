from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from .models import Category, Page

from .forms import CategoryForm, PageForm

def index(request):
	cat = Category.objects.order_by('-likes')[:5]
	pages = Page.objects.order_by('-views')[:5]
	context_dict = {'categories': cat,
					'pages': pages}
	return render(request, 'rango/index.html', context_dict)

def about(request):
	context_dict = {'msg': 'hello dear friends'}
	return render(request, 'rango/about.html', context = context_dict)


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

def add_category(request):
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save(commit = True)
			return index(request)
	else:
		form = CategoryForm()
	return render(request, 'rango/add_category.html', {'form': form})

def add_page(request, category_name_url):
	cat = get_object_or_404(Category, slug = category_name_url)
	if request.method == 'POST':
		form = PageForm(request.POST)
		if form.is_valid():
			page = form.save(commit = False)
			page.category = cat
			page.save()
			return index(request)
	else:
		form = PageForm()
	context_dict = {'form': form, 'cat': cat}
	return render(request, 'rango/add_page.html', context_dict)