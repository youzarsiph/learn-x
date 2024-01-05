""" API endpoints for learn_x.courses """


from typing import Any
from django.http import FileResponse, HttpRequest
from django.views.generic import DetailView
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from learn_x.courses.models import Course
from learn_x.courses.serializers import CourseSerializer


# Create your views here.
class CourseViewSet(ModelViewSet):
    """Create, view, update and delete Courses"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    search_fields = ["name", "headline", "description"]
    ordering_fields = ["id", "name", "created_at", "updated_at"]
    filterset_fields = ["name"]

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            self.permission_classes = [permissions.IsAuthenticatedOrReadOnly]

        return super().get_permissions()


class CourseImageView(DetailView):
    """Course profile image"""

    model = Course

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> FileResponse:
        return FileResponse(open(self.get_object(self.queryset).image.url[1:], "rb"))
