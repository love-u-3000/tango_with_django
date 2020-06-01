import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django.settings')

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
	page = Page(category = cat, title = page_title, url = page_url)
	page.save()

def add_category(cat_name):
	cat = Category(name = cat_name)
	cat.save()
	return cat

if __name__ == '__main__':
	print("Starting Rango population script...")
	populate()