from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.http import StreamingHttpResponse, Http404
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
import mimetypes
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .serializers import PostDetailSerializer, PostListSerializer
from .models import Post
from .pagination import PostLimitOffsetPagination

MODEL_CONFIG = {
    'post': {'model': Post, 'field': 'photo'},
}


@api_view(['GET'])
@permission_classes([AllowAny])
def serve_universal_image(request, model_type, pk):
    config = MODEL_CONFIG.get(model_type)
    if not config:
        raise Http404("Invalid resource type")

    model_class = config['model']
    field_name = config['field']
    obj = get_object_or_404(model_class, pk=pk)
    image_field = getattr(obj, field_name)

    if not image_field:
        return Response({'message': 'Object has no image'}, status=status.HTTP_404_NOT_FOUND)


    try:
        file_handle = image_field.open(mode='rb')
        
        content_type, _ = mimetypes.guess_type(image_field.name)
        if content_type is None:
            content_type = 'application/octet-stream'

        response = StreamingHttpResponse(file_handle, content_type=content_type)
        response['Content-Length'] = image_field.size
        response['Content-Disposition'] = f'inline; filename="{image_field.name.split("/")[-1]}"'
        
        return response
    except Exception as e:
        print(f"Error serving file from S3 storage: {e}")
        
        return Response(
            {"error": "File could not be retrieved from storage."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


class ListPostAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    pagination_class = PostLimitOffsetPagination
    
class DetailPostAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    lookup_field = "slug"
    serializer_class = PostDetailSerializer