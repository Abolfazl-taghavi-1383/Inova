from django.db import models
from django.shortcuts import reverse
import uuid


from .utils import rename_image, unique_slugify

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    photo = models.ImageField(upload_to=rename_image, blank=True, null=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    body = models.TextField()
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False) 
    
    
    def __str__(self):
        return self.title

    def get_api_url(self):
        try:
            return reverse("blog:post_detail", kwargs={"slug": self.slug})
        except:
            None
            
    def save(self, *args, **kwargs):
        unique_slugify(self, self.title) 
        super().save(*args, **kwargs)
