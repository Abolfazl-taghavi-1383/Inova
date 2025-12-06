from django.contrib import admin

from .views import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['slug'] 