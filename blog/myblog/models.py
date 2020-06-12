from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	title = models.CharField(max_length = 500, unique = True)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank = True, null = True)

	def __str__(self):
		return self.title
