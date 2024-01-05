""" Data Models for learn_x.courses """


from django.db import models


# Create your models here.
class Course(models.Model):
    """Courses"""

    image = models.ImageField(
        upload_to="images/courses/",
        help_text="Course image",
    )
    name = models.CharField(
        max_length=64,
        unique=True,
        db_index=True,
        help_text="Course name",
    )
    headline = models.CharField(
        max_length=128,
        db_index=True,
        help_text="Course headline",
    )
    description = models.CharField(
        max_length=256,
        db_index=True,
        help_text="Course description",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Date updated",
    )

    def __str__(self) -> str:
        return self.name
