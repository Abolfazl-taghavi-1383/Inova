from django.utils.text import slugify
import os
import uuid


from .models import Post

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

# Generate random image name by uuid and make clean path
def rename_image(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f'{uuid.uuid4().hex}.{ext}'
    return os.path.join(f'{instance.__class__.__name__.lower()}_images', new_filename)