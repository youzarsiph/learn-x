""" Serializers for learn_x.modules """


from rest_framework.serializers import HyperlinkedModelSerializer
from learn_x.modules.models import Module


# Create your serializers here.
class ModuleSerializer(HyperlinkedModelSerializer):
    """Module serializer"""

    class Meta:
        """Meta data"""

        model = Module
        read_only_fields = ["course"]
        fields = [
            "id",
            "url",
            "course",
            "title",
            "description",
            "created_at",
            "updated_at",
        ]
