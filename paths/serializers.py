""" Serializers for learn_x.paths """

from rest_framework.serializers import ModelSerializer
from learn_x.paths.models import Path


# Create your serializers here.
class PathSerializer(ModelSerializer):
    """Path serializer"""

    class Meta:
        """Meta data"""

        model = Path
        fields = [
            "id",
            "url",
            "image",
            "name",
            "headline",
            "description",
            "created_at",
            "updated_at",
            "courses",
            "projects",
        ]


class DetailedPathSerializer(PathSerializer):
    """Path serializer"""

    class Meta(PathSerializer.Meta):
        """Meta data"""

        depth = 1
