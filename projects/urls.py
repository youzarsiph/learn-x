""" URLConf for learn_x.projects """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from learn_x.projects.views import ProjectViewSet, ProjectImageView


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("projects", ProjectViewSet, "project")

urlpatterns = [
    path("", include(router.urls)),
    path("projects/<int:pk>/image", ProjectImageView.as_view()),
]
