from django.db.models.signals import pre_save

from .functions import create_slug
from .models import Post

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
        
pre_save.connect(pre_save_post_receiver, sender=Post)