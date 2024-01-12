""" Data Models for learn_x.items """


from django.db import models


# Create your models here.
class Item(models.Model):
    """Items"""

    module = models.ForeignKey(
        "modules.Module",
        on_delete=models.CASCADE,
        related_name="items",
        help_text="Item module",
    )
    title = models.CharField(
        max_length=64,
        help_text="Item title",
    )
    content = models.JSONField(
        help_text="Item content",
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
        return self.title
