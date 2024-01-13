""" Data Models for learn_x.paths """


from django.db import models


# Create your models here.
class Path(models.Model):
    """Learning Paths"""

    image = models.ImageField(
        upload_to="images/paths/",
        help_text="Path image",
    )
    name = models.CharField(
        max_length=64,
        unique=True,
        db_index=True,
        help_text="Path name",
    )
    headline = models.CharField(
        max_length=128,
        db_index=True,
        help_text="Path headline",
    )
    description = models.CharField(
        max_length=256,
        db_index=True,
        help_text="Path description",
    )
    courses = models.ManyToManyField(
        "courses.Course",
        help_text="Learning path courses",
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
