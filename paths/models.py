""" Data Models for learn_x.paths """

from django.db import models


# Create your models here.
class Path(models.Model):
    """Career Paths"""

    image = models.ImageField(
        null=True,
        blank=True,
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
        max_length=512,
        db_index=True,
        help_text="Path headline",
    )
    description = models.CharField(
        max_length=1024,
        db_index=True,
        help_text="Path description",
    )
    courses = models.ManyToManyField(
        "courses.Course",
        blank=True,
        help_text="Career path courses",
    )
    projects = models.ManyToManyField(
        "projects.Project",
        blank=True,
        help_text="Career path projects",
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
