""" Data Models for learn_x.courses """

from django.db import models


# Create your models here.
class Course(models.Model):
    """Courses"""

    image = models.ImageField(
        null=True,
        blank=True,
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
        max_length=512,
        db_index=True,
        help_text="Course headline",
    )
    description = models.CharField(
        max_length=1024,
        db_index=True,
        help_text="Course description",
    )
    projects = models.ManyToManyField(
        "projects.Project",
        blank=True,
        help_text="Course projects",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Date updated",
    )

    @property
    def module_count(self) -> int:
        """Number of modules"""

        return self.modules.count()

    @property
    def item_count(self) -> int:
        """Number of items"""

        return sum([module.items.count() for module in self.modules.all()])

    def __str__(self) -> str:
        return self.name
