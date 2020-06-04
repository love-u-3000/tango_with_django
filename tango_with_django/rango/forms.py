from django import forms
from rango.models import Category, Page

class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length = 128, help_text = 'Please enter the name of Category')
	views = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
	likes = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
	slug = forms.CharField(widget = forms.HiddenInput(), required = False)

	class Meta:
		model = Category
		fields = ('name', )

class PageForm(forms.ModelForm):
	title = forms.CharField(max_length = 128, help_text = 'Please enter the title of the Page')
	views = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
	url = forms.URLField(max_length = 200, help_text = 'Please enter the url for the Page')

	class Meta:
		model = Page
		exclude = ('category', )