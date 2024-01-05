""" Serializers for learn_x.projects """


from rest_framework.serializers import HyperlinkedModelSerializer
from learn_x.projects.models import Project


# Create your serializers here.
class ProjectSerializer(HyperlinkedModelSerializer):
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
