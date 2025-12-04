from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save
import uuid
import os

def rename_image(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f'{uuid.uuid4().hex}.{ext}'
    return os.path.join(f'{instance.__class__.__name__.lower()}_images', new_filename)


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    photo = models.ImageField(upload_to=rename_image, blank=True, null=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False) 
    
    
    def __str__(self):
        return self.title

    def get_api_url(self):
        try:
            return reverse("posts_api:post_detail", kwargs={"slug": self.slug})
        except:
            None

# Recursive Function to generate unique slug
def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    
    if new_slug is not None:
        slug = new_slug
        
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
        
pre_save.connect(pre_save_post_receiver, sender=Post)
