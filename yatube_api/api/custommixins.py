from rest_framework import viewsets, mixins


class CreateMixin(mixins.CreateModelMixin, viewsets.GenericViewSet):
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FollowMixin(mixins.CreateModelMixin, mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    pass
