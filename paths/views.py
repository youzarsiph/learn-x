""" API endpoints for learn_x.paths """


from typing import Any
from django.http import FileResponse, HttpRequest
from django.views.generic import DetailView
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from learn_x.paths.models import Path
from learn_x.paths.serializers import DetailedPathSerializer, PathSerializer


# Create your views here.
class PathViewSet(ModelViewSet):
    """Create, view, update and delete Paths"""

    queryset = Path.objects.all()
    serializer_class = DetailedPathSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    search_fields = ["name", "headline", "description"]
    ordering_fields = ["id", "name", "created_at", "updated_at"]
    filterset_fields = ["name"]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            self.serializer_class = PathSerializer

        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            self.permission_classes = [permissions.IsAuthenticatedOrReadOnly]

        return super().get_permissions()


class PathImageView(DetailView):
    """Path profile image"""

    model = Path

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> FileResponse:
        return FileResponse(open(self.get_object(self.queryset).image.url[1:], "rb"))
