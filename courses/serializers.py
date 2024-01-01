""" Serializers for learn_x.courses """


from rest_framework.serializers import HyperlinkedModelSerializer
from learn_x.courses.models import Course


# Create your serializers here.
class CourseSerializer(HyperlinkedModelSerializer):
    """Course serializer"""

    class Meta:
        """Meta data"""

        model = Course
        fields = [
            "id",
            "url",
        ]
