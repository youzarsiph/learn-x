""" URLConf for learn_x """


from django.urls import path, include
from rest_framework.routers import DefaultRouter


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)

sub_router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("", include("learn_x.courses")),
    path("", include("learn_x.items")),
    path("", include("learn_x.modules")),
    path("", include("learn_x.projects")),
]
