""" API endpoints for learn_x.projects """


from typing import Any
from django.http import FileResponse, HttpRequest
from django.views.generic import DetailView
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from learn_x.permissions import IsReadOnly
from learn_x.paths.models import Path
from learn_x.courses.models import Course
from learn_x.projects.models import Project
from learn_x.projects.serializers import ProjectSerializer


# Create your views here.
class ProjectViewSet(ModelViewSet):
    """Create, view, update and delete Projects"""

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    search_fields = ["name", "description", "content"]
    ordering_fields = ["id", "name", "created_at", "updated_at"]
    filterset_fields = ["name"]


class ProjectImageView(DetailView):
    """Project profile image"""

    model = Project

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> FileResponse:
        return FileResponse(open(self.get_object(self.queryset).image.url[1:], "rb"))


class CourseProjectsViewSet(ProjectViewSet):
    """Course Projects"""

    permission_classes = [
        IsReadOnly,
        permissions.IsAuthenticated,
        permissions.IsAdminUser,
    ]

    def get_queryset(self):
        """Filter queryset by course"""

        course = Course.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(course=course)


class PathProjectsViewSet(ProjectViewSet):
    """Learning Path Projects"""

    permission_classes = [
        IsReadOnly,
        permissions.IsAuthenticated,
        permissions.IsAdminUser,
    ]

    def get_queryset(self):
        """Filter queryset by learning path"""

        path = Path.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(path=path)
