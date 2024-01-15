""" API endpoints for learn_x.courses """


from typing import Any
from django.http import FileResponse, HttpRequest
from django.views.generic import DetailView
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from learn_x.permissions import IsReadOnly
from learn_x.courses.models import Course
from learn_x.courses.serializers import DetailedCourseSerializer, CourseSerializer
from learn_x.paths.models import Path


# Create your views here.
class CourseViewSet(ModelViewSet):
    """Create, view, update and delete Courses"""

    queryset = Course.objects.all()
    serializer_class = DetailedCourseSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    search_fields = ["name", "headline", "description"]
    ordering_fields = ["id", "name", "created_at", "updated_at"]
    filterset_fields = ["name"]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            self.serializer_class = CourseSerializer

        return super().get_serializer_class()


class CourseImageView(DetailView):
    """Course profile image"""

    model = Course

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> FileResponse:
        return FileResponse(open(self.get_object(self.queryset).image.url[1:], "rb"))


class PathCoursesViewSet(CourseViewSet):
    """Courses of a learning path"""

    permission_classes = [
        IsReadOnly,
        permissions.IsAuthenticated,
        permissions.IsAdminUser,
    ]

    def get_queryset(self):
        """Filter queryset by path"""

        path = Path.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(path=path)
