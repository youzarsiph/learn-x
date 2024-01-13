""" URLConf for learn_x.paths """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from learn_x.paths.views import PathViewSet, PathImageView
from learn_x.courses.views import PathCoursesViewSet
from learn_x.projects.views import PathProjectsViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("paths", PathViewSet, "path")

sub_router = DefaultRouter(trailing_slash=False)
sub_router.register("courses", PathCoursesViewSet, "course")
sub_router.register("projects", PathProjectsViewSet, "project")

urlpatterns = [
    path("", include(router.urls)),
    path("paths/<int:pk>/image", PathImageView.as_view()),
    path(
        "paths/<int:id>/",
        include((sub_router.urls, "paths"), namespace="paths"),
    ),
]
