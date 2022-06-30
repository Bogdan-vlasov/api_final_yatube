from django.urls import path, include
from rest_framework.routers import DefaultRouter


from api.views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

v1_router = DefaultRouter()

v1_router.register(r'^posts', PostViewSet)
v1_router.register(r'^posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comments')
v1_router.register(r'^groups', GroupViewSet, basename="group")
v1_router.register(r'^follow', FollowViewSet, basename="follow")

urlpatterns = [
    path('v1/', include('djoser.urls.jwt',)),
    path('v1/', include(v1_router.urls)),
]
