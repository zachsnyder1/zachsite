"""
Models for zachsite app.
"""

from django.db import models


class QuestionAndAnswer(models.Model):
    """
    Questions and their answers for the QA Carousel
    on the Spiel page.
    """
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=120)
    answer = models.CharField(max_length=120)

    def __str__(self):
        return self.question
