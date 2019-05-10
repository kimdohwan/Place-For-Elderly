from django.contrib.auth.models import AbstractUser
from django.db import models

Facility = 'facilities.Facility'


class User(AbstractUser):
    likes = models.ForeignKey(
        Facility,
        on_delete=models.CASCADE,
        related_name='facilities',
        null=True,
    )
