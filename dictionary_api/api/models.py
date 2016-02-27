from __future__ import unicode_literals

from django.db import models

# ORM - Object Relational Mapper

class Word(models.Model):
	title = models.CharField(max_length=50)
	definition = models.CharField(max_length=25)
	language = models.CharField(max_length=25)

	def __unicode__(self):
		return self.title
