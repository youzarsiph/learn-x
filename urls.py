""" URLConf for LearnX """


from django.urls import path, include
from rest_framework.routers import DefaultRouter


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)

urlpatterns = [
    path("", include(router.urls)),
    path("", include("learn_x.courses.urls")),
    path("", include("learn_x.items.urls")),
    path("", include("learn_x.modules.urls")),
    path("", include("learn_x.projects.urls")),
    path("", include("learn_x.paths.urls")),
]
