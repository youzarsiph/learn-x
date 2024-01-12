""" Serializers for learn_x.modules """


import copy
from rest_framework.serializers import ModelSerializer
from learn_x.modules.models import Module


# Create your serializers here.
class ModuleSerializer(ModelSerializer):
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


class DetailedModuleSerializer(ModuleSerializer):
    """Module serializer with items serialized"""

    class Meta(ModuleSerializer.Meta):
        """Meta data"""

        depth = 1
        temp_fields = copy.deepcopy(ModuleSerializer.Meta.fields)
        temp_fields.remove("course")
        fields = temp_fields + [
            "items",
        ]
