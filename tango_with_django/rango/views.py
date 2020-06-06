from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Category, Page, UserProfile
from .forms import CategoryForm, PageForm, UserForm, UserProfileForm
from django.contrib.auth import login, authenticate
from django.urls import reverse

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
			return HttpResponseRedirect(reverse('rango:index'))
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
			return HttpResponseRedirect(reverse('rango:category', kwargs={'category_name_url': category_name_url}))
	else:
		form = PageForm()
	context_dict = {'form': form, 'cat': cat}
	return render(request, 'rango/add_page.html', context_dict)

def register(request):

	registered = False

	if request.method == 'POST':
		user_form = UserForm(request.POST)
		profile_form = UserProfileForm(request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save(commit = False)
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit = False)
			profile.user = user

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.save()
			registered = True	

	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	context_dict = {'user_form': user_form,
					'profile_form': profile_form,
					'registered': registered}
	return render(request, 'rango/register.html', context_dict)

def user_login(request, prompt = False):
	if request.method == 'POST' and not prompt:
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username = username, password = password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('rango:index'))
			else:
				return HttpResponse("Account is disabled")
		else:
			return user_login(request, True)
	else:
		return render(request, 'rango/login.html', {'prompt': prompt})
