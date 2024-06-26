""" Data Models for learn_x.projects """

from django.db import models


# Create your models here.
class Project(models.Model):
    """Projects"""

    image = models.ImageField(
        null=True,
        blank=True,
        upload_to="images/projects/",
        help_text="Project image",
    )
    name = models.CharField(
        max_length=64,
        unique=True,
        db_index=True,
        help_text="Project name",
    )
    description = models.CharField(
        max_length=1024,
        help_text="Project description",
    )
    content = models.TextField(
        help_text="Project content",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update",
    )

    def __str__(self) -> str:
        return self.name
