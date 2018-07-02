from django.db import models

# Create your models here.

class TimeStampledModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: # This is not variable things
        abstract = True # Make abstarct base class option


class Image(TimeStampledModel):

    file = models.ImageField()
    location = models.CharField(max_length = 140)
    caption = models.TextField()

class Comment(TimeStampledModel):

    message = models.TextField()