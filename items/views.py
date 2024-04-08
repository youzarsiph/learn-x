""" API endpoints for learn_x.items """

from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from learn_x.permissions import IsReadOnly
from learn_x.courses.models import Course
from learn_x.items.models import Item
from learn_x.items.serializers import ItemSerializer
from learn_x.modules.models import Module


# Create your views here.
class ItemViewSet(ModelViewSet):
    """List and retrieve Items"""

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [
        IsReadOnly,
        permissions.IsAuthenticated,
        permissions.IsAdminUser,
    ]
    search_fields = ["title"]
    ordering_fields = ["id", "created_at", "updated_at"]
    filterset_fields = ["title"]

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            self.permission_classes = [permissions.IsAuthenticatedOrReadOnly]

        return super().get_permissions()


class CourseItemsViewSet(ItemViewSet):
    """List and retrieve Course Items"""

    def get_queryset(self):
        """Filter queryset by course"""

        course = Course.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(module__course=course)


class ModuleItemsViewSet(ItemViewSet):
    """Create, read, update and delete Module Items"""

    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get_queryset(self):
        """Filter queryset by Module"""

        module = Module.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(module=module)

    def perform_create(self, serializer):
        """Add Module to Item"""

        module = Module.objects.get(pk=self.kwargs["id"])
        serializer.save(module=module)
