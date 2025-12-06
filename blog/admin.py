from django.contrib import admin

from .views import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'slug')
    search_fields = ('title', )
    readonly_fields = ('slug', ) 