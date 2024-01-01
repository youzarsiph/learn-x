""" Serializers for learn_x.items """


from rest_framework.serializers import HyperlinkedModelSerializer
from learn_x.items.models import Item


# Create your serializers here.
class ItemSerializer(HyperlinkedModelSerializer):
    """Item serializer"""

    class Meta:
        """Meta data"""

        model = Item
        fields = [
            "id",
            "url",
        ]
