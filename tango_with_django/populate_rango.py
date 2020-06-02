import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django.settings')

import random

import django
django.setup()
from rango.models import Category, Page

def populate():
	python_pages = [
		{"title": "Official Python Tutorial",
		"url":"http://docs.python.org/2/tutorial/"},
		{"title":"How to Think like a Computer Scientist",
		"url":"http://www.greenteapress.com/thinkpython/"},
		{"title":"Learn Python in 10 Minutes",
		"url":"http://www.korokithakis.net/tutorials/python/"} ]

	django_pages = [
		{"title":"Official Django Tutorial",
		"url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
		{"title":"Django Rocks",
		"url":"http://www.djangorocks.com/"},
		{"title":"How to Tango with Django",
		"url":"http://www.tangowithdjango.com/"} ]

	other_pages = [
		{"title":"Bottle",
		"url":"http://bottlepy.org/docs/dev/"},
		{"title":"Flask",
		"url":"http://flask.pocoo.org"} ]

	categories = {"Python": {"pages": python_pages},
				  "Django": {"pages": django_pages},
				  "Other Frameworks": {"pages": other_pages}
				  }
	for cat_name, data in categories.items():
		cat = add_category(cat_name)
		for page in data["pages"]:
			add_page(cat, page["title"], page["url"])

	for c in Category.objects.all():
		for p in Page.objects.filter(category=c):
			print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, page_title, page_url):
	page = Page.objects.get_or_create(category = cat, title = page_title, url = page_url)[0]
	page.views = random.randint(0,100)
	page.save()

def add_category(cat_name):
	cat = Category.objects.get_or_create(name = cat_name)[0]
	if cat_name == "Python":
		cat.views = 128
		cat.likes = 64
	elif cat_name == "Django":
		cat.views = 64
		cat.likes = 32
	else:
		cat.views = 32
		cat.likes = 16
	cat.save()
	return cat

if __name__ == '__main__':
	print("Starting Rango population script...")
	populate()