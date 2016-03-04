from __future__ import unicode_literals

from django.db import models

# ORM - Object Relational Mapper

class Word(models.Model):
	title = models.CharField(max_length=50)
	definition = models.CharField(max_length=200, blank=True)
	language = models.CharField(max_length=10)
	translations = models.ManyToManyField('Word', blank=True, related_name='translation')
	synonyms = models.ManyToManyField('Word', blank=True, related_name='synonym')
	antonyms = models.ManyToManyField('Word', blank=True, related_name='antonym')

	def __unicode__(self):
		return self.title
