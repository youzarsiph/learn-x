""" Serializers for learn_x.projects """


from rest_framework.serializers import HyperlinkedModelSerializer
from learn_x.projects.models import Project


# Create your serializers here.
class ProjectSerializer(HyperlinkedModelSerializer):
    """Project serializer"""

    class Meta:
        """Meta data"""

        model = Project
        fields = [
            "id",
            "url",
        ]
