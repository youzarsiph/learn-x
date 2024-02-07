""" URLConf for learn_x.courses """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from learn_x.courses.views import CourseViewSet
from learn_x.items.views import CourseItemsViewSet
from learn_x.modules.views import CourseModulesViewSet
from learn_x.projects.views import CourseProjectsViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("courses", CourseViewSet, "course")

sub_router = DefaultRouter(trailing_slash=False)
sub_router.register("items", CourseItemsViewSet, "item")
sub_router.register("modules", CourseModulesViewSet, "module")
sub_router.register("projects", CourseProjectsViewSet, "project")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "courses/<int:id>/",
        include((sub_router.urls, "courses"), namespace="courses"),
    ),
]
