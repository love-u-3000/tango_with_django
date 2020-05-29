from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	return HttpResponse("<html><body><h1>hello from rango</h1><body><html>")
