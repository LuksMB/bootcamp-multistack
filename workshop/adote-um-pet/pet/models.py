from django.db import models


class Pet(models.Model):
    name = models.CharField(blank=False, null=False, max_length=255)
    bio = models.TextField(blank=False, null=False)
    img_address = models.URLField(blank=False, null=False)
