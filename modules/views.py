""" API endpoints for learn_x.modules """

from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from learn_x.permissions import IsReadOnly
from learn_x.courses.models import Course
from learn_x.modules.models import Module
from learn_x.modules.serializers import DetailedModuleSerializer, ModuleSerializer


# Create your views here.
class ModuleViewSet(ModelViewSet):
    """List and retrieve Course Modules"""

    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [
        IsReadOnly,
        permissions.IsAuthenticated,
        permissions.IsAdminUser,
    ]
    search_fields = ["title", "description"]
    ordering_fields = ["id", "title", "created_at", "updated_at"]
    filterset_fields = ["title", "course"]

    def get_serializer_class(self):
        if self.action == "retrieve":
            self.serializer_class = DetailedModuleSerializer

        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            self.permission_classes = [permissions.IsAuthenticatedOrReadOnly]

        return super().get_permissions()


class CourseModulesViewSet(ModuleViewSet):
    """Create, read, update and delete Course Modules"""

    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get_queryset(self):
        """Filter queryset by course"""

        course = Course.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(course=course)

    def perform_create(self, serializer):
        """Add course to module"""

        course = Course.objects.get(pk=self.kwargs["id"])
        serializer.save(course=course)
