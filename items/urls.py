""" URLConf for learn_x.items """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from learn_x.items.views import ItemViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("items", ItemViewSet, "item")

urlpatterns = [
    path("", include(router.urls)),
]
