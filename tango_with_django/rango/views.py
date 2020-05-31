from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake"}
	return render(request, 'rango/index.html', context = context_dict)

def about(request):
	response = "<html><body><h1>Welcome to about us page</h1>"
	response += "<a href = 'http://127.0.0.1:8000/rango' >Main Page</a></body></html>"
	return HttpResponse(response)