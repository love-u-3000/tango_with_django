from django.db import models

from django.template.defaultfilters import slugify

from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length = 128, unique = True)
	views = models.IntegerField(default = 0)
	likes = models.IntegerField(default = 0)
	slug = models.SlugField(blank = True, unique = True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name
	
class Page(models.Model):
	views = models.IntegerField(default = 0)
	title = models.CharField(max_length = 128)
	category = models.ForeignKey('Category', on_delete = models.CASCADE)
	url = models.URLField()

	class Meta:
		verbose_name_plural = 'All Pages'

	def __str__(self):
		return self.title

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	website = models.URLField(blank = True)
	picture = models.ImageField(upload_to = 'profile_images', blank = True)

	def __str__(self):
		return self.user.username
