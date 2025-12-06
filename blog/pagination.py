from rest_framework.pagination import (
    LimitOffsetPagination,
)

class PostLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 6
    max_limit = 6