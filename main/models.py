from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='media', height_field=None, width_field=None, max_length=None)
    rating = models.CharField(max_length=250)
    genres = models.CharField(max_length=250)

    def __str__(self):
        return self.title
    
