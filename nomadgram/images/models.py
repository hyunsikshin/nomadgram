from django.db import models
from nomadgram.users import models as user_models

# Create your models here.

class TimeStampledModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: # This is not variable things
        abstract = True # Make abstarct base class option


class Image(TimeStampledModel):

    """ Image Model """

    file = models.ImageField()
    location = models.CharField(max_length = 140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User, null = True, on_delete = models.CASCADE)

class Comment(TimeStampledModel):

    """ Comment Model """

    message = models.TextField()
    creator = models.ForeignKey(user_models.User, null = True, on_delete = models.CASCADE)
    image = models.ForeignKey(Image, null = True, on_delete = models.CASCADE)

class Like(TimeStampledModel):

    """ Like Model """

    creator = models.ForeignKey(user_models.User, null = True, on_delete = models.CASCADE)
    image = models.ForeignKey(Image, null = True, on_delete = models.CASCADE)
