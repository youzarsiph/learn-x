""" Data Models for learn_x.modules """

from django.db import models


# Create your models here.
class Module(models.Model):
    """Modules"""

    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        related_name="modules",
        help_text="Module course",
    )
    title = models.CharField(
        max_length=64,
        help_text="Module name",
    )
    description = models.CharField(
        max_length=1024,
        help_text="Module description",
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
    def item_count(self) -> int:
        """Number of items"""

        return self.items.count()

    def __str__(self) -> str:
        return f"{self.course} {self.title}"
