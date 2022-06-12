from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,
                                        IsAuthenticated)
from rest_framework.filters import SearchFilter

from posts.models import Post, Group, Follow
from .permissions import AuthorOrReadOnlyPermission
from .serializers import (FollowSerializer, PostSerializer,
                          GroupSerializer, CommentSerializer)
from .custommixins import CreateMixin, FollowMixin


class PostViewSet(CreateMixin, viewsets.ModelViewSet):
    permission_classes = [AuthorOrReadOnlyPermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(CreateMixin, viewsets.ModelViewSet):
    permission_classes = [AuthorOrReadOnlyPermission]
    serializer_class = CommentSerializer

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return post.comments.all()


class FollowViewSet(FollowMixin):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,)
    pagination_class = LimitOffsetPagination
    search_fields = (r'following__username',)  # r'[\w]*')

    def get_queryset(self):
        queryset = Follow.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
