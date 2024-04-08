""" Serializers for LearnX """

from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer


# Create your serializers here.
User = get_user_model()


class UserSerializer(ModelSerializer):
    """User Serializer"""

    class Meta:
        """Meta data"""

        model = User
        fields = [
            "id",
            "url",
            "username",
            "first_name",
            "last_name",
            "email",
            "date_joined",
            "last_login",
        ]
