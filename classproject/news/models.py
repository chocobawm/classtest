from django.db import models

class newStory(models.Model):
    heading_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    story_text = models.CharField(max_length=5000)
