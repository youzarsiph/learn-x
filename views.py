""" API endpoints for LearnX """

from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from learn_x.serializers import UserSerializer


# Create your views here.
User = get_user_model()


class UserViewSet(ModelViewSet):
    """User ViewSet"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
