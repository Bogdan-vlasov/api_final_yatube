from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (AllowAny,
                                        IsAuthenticated)
from rest_framework.filters import SearchFilter

from posts.models import Post, Group, Follow, Comment
from .permissions import AuthorOrReadOnlyPermission
from .serializers import (FollowSerializer, PostSerializer,
                          GroupSerializer, CommentSerializer)



class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [AuthorOrReadOnlyPermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer): 
        serializer.save(author=self.request.user) 
    
    def get_post(self):
        get_object_or_404(Post, pk=self.kwargs.get('post_id'))


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnlyPermission,)
    
    def get_post(self, model):
        obj = get_object_or_404(model, pk=self.kwargs.get('post_id'))
        return obj
        
    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post(Post))

    def get_queryset(self):
        return self.get_post(Post).comments


class FollowViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,)
    pagination_class = LimitOffsetPagination
    search_fields = ('following__username', 'user__username')

    def get_queryset(self):
        queryset = Follow.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
