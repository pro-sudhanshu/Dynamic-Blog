from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=255)
    post_img = models.URLField(max_length=500, null=True, blank=True)
    post_content = models.TextField()
    post_category = models.CharField(max_length=100, choices=(
        ('Technology','Technology'), ('Education','Education'), ('Crypto','Crypto')
        ), default='Technology')
    post_published_date = models.DateTimeField(auto_now_add=True, blank=True)
    post_slug = AutoSlugField(populate_from='post_title', unique=True, always_update=True)

    def __str__(self):
        return self.post_title