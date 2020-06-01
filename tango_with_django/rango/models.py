from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length = 128, unique = True)
	visits = models.IntegerField(default = 0)

	def __str__(self):
		return self.name
	
class Page(models.Model):
	views = models.IntegerField(default = 0)
	title = models.CharField(max_length = 128)
	category = models.ForeignKey('Category', on_delete = models.CASCADE)
	url = models.URLField()

	def __str__(self):
		return self.title
				