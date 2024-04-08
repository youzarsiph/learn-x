""" URLConf for learn_x.modules """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from learn_x.modules.views import ModuleViewSet
from learn_x.items.views import ModuleItemsViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("modules", ModuleViewSet, "module")

sub_router = DefaultRouter(trailing_slash=False)
sub_router.register("items", ModuleItemsViewSet, "item")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "modules/<int:id>/",
        include((sub_router.urls, "modules"), namespace="modules"),
    ),
]
