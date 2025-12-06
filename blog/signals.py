from django.db.models.signals import pre_save

from .utils import unique_slugify
from .models import Post

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug_str = instance.title
        instance.slug = unique_slugify(instance, slug_str) 
        
pre_save.connect(pre_save_post_receiver, sender=Post)