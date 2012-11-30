import datetime
from django.db import models

class News(models.Model):
	title  = models.CharField(max_length=200)
	text   = models.CharField(max_length=2000)
#	author = 
	pub_date = models.DateTimeField('date published')
	def __unicode__(self):
		return self.text
