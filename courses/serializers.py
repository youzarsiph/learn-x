""" Serializers for learn_x.courses """


from rest_framework.serializers import ModelSerializer
from learn_x.courses.models import Course


# Create your serializers here.
class CourseSerializer(ModelSerializer):
    """Course serializer"""

    class Meta:
        """Meta data"""

        model = Course
        fields = [
            "id",
            "url",
            "image",
            "name",
            "headline",
            "description",
            "created_at",
            "updated_at",
        ]


class DetailedCourseSerializer(CourseSerializer):
    """Course serializer"""

    class Meta(CourseSerializer.Meta):
        """Meta data"""

        depth = 1
        fields = CourseSerializer.Meta.fields + [
            "modules",
            "projects",
        ]
