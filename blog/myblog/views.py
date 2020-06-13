from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from myblog.models import Post
from myblog.forms import PostForm, UserForm
from django.utils import timezone

posts = None

def index(request):
	global posts
	if request.user.is_active:
		posts = Post.objects.filter(author = request.user).order_by('-published_date')
	context_dict = {'posts': posts}
	return render(request, 'myblog/index.html', context_dict)

def register(request):
	if request.method == 'POST':
		user_form = UserForm(request.POST)
		if user_form.is_valid():
			user = user_form.save(commit = True)
			user.set_password(user.password)
			user.save()
			return HttpResponseRedirect(reverse('myblog:login'))
	else:
		user_form = UserForm()
	context_dict = {'user_form': user_form}
	return render(request, 'myblog/register.html', context_dict)


def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		global posts
		user = authenticate(username = username, password = password)
		if user:
			if user.is_active:
				login(request, user)
				posts = Post.objects.filter(author = user).order_by('-published_date')
				return HttpResponseRedirect(reverse('myblog:index'))
			else:
				return HttpResponse("Your account is disabled")
		else:
			return HttpResponse("Please enter valid credentials")
	else:
		return render(request, 'myblog/login.html', {})
		
def user_logout(request):
	logout(request)
	global posts
	posts = None
	return HttpResponseRedirect(reverse('myblog:index'))

def addpost(request):
	if request.method == 'POST':
		post_form = PostForm(request.POST)
		if post_form.is_valid():
			post = post_form.save(commit = False)
			post.published_date = timezone.now();
			post.author = request.user
			post.save()
			global posts
			posts = Post.objects.filter(author = request.user).order_by('-published_date')
			return HttpResponseRedirect(reverse('myblog:index'))
		else:
			context_dict = {'post_form': post_form}
			return render(request, 'myblog/addpost.html', context_dict)
	else:
		post_form = PostForm()
		context_dict = {'post_form': post_form}
		return render(request, 'myblog/addpost.html', context_dict)

def editpost(request, pk):
	post = Post.objects.get(pk = pk)
	if request.method == 'POST':
		post.delete()
		return addpost(request)

	else:
		post_form = PostForm({'title': post.title, 'text': post.text})
		context_dict = {'post_form': post_form, 'pk': pk}
		return render(request, 'myblog/addpost.html', context_dict)

