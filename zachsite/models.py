from django.db import models


class QuestionAndAnswer(models.Model):
	"""
	Questions and their answers for the QA Carousel
	on the Spiel page.
	"""
	question = models.CharField(max_length=120)
	answer = models.CharField(max_length=120)
	
	def __str__(self):
		return self.question


class Blurb(models.Model):
	"""
	Blurbs for the info section of the Spiel page.
	"""
	title = models.CharField(max_length=80)
	text = models.TextField()
	
	def __str__(self):
		return self.title