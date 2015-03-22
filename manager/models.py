from django.db import models
# Create your models here.

class Paste(models.Model):
	title = models.CharField(max_length=200)
	code = models.TextField()
	createdat = models.DateTimeField(auto_now_add=True)
	category = models.CharField(max_length=200)
	def __unicode__(self):
		return self.title