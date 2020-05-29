from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	response = "<html><body><h1>Rango says hello!</h1>"
	response += "<a href = 'http://127.0.0.1:8000/rango/about' >About us</a></body></html>"
	return HttpResponse(response)

def about(request):
	response = "<html><body><h1>Welcome to about us page</h1>"
	response += "<a href = 'http://127.0.0.1:8000/rango' >Main Page</a></body></html>"
	return HttpResponse(response)