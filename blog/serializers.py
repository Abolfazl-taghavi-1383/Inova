from rest_framework import serializers
from .models import Post, Comment


class PostListSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "id",
            "url",
            "title",
            "description",
            "created_at"
        ]

    def get_url(self, obj):
        return obj.get_api_url()
    
class PostDetailSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "slug",
            "title",
            "description",
            "body",
            "author",
            "image",
            "created_at",
            "updated_at",
            "comments",
        ]

    def get_slug(self, obj):
        return obj.slug


