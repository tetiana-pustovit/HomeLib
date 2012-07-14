from django.db import models

# Create your models here.
# add fields: id, name, genre, description
class Movies(models.Model):
	name = models.CharField(max_length=150)
	genre = models.CharField(max_length=50)
	description = models.CharField(max_length=1500)
	def __unicode__(self):
		return self.name