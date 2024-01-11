""" Serializers for learn_x.projects """


from rest_framework.serializers import ModelSerializer
from learn_x.projects.models import Project


# Create your serializers here.
class ProjectSerializer(ModelSerializer):
    """Project serializer"""

    class Meta:
        """Meta data"""

        model = Project
        read_only_fields = ["course"]
        fields = [
            "id",
            "url",
            "course",
            "name",
            "description",
            "content",
            "created_at",
            "updated_at",
        ]
