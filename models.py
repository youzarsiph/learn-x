""" Data Models for LearnX """

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    """Learn Users"""

    image = models.ImageField(
        null=True,
        blank=True,
        help_text="Profile image",
        upload_to="images/users/",
    )
