from django.db import models


class Adoption(models.Model):
    value = models.DecimalField(blank=False, null=False, max_digits=5, decimal_places=2)
    email = models.EmailField(blank=False, null=False, max_length=255)
    pet = models.ForeignKey(to="pet.Pet", null=False, on_delete=models.CASCADE)
