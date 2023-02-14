from django.db import models
from django.core.validators import MinValueValidator
import decimal

class Item(models.Model):
    name = models.CharField(max_length=256, verbose_name="name")
    description = models.TextField(blank=True, verbose_name="description")
    price = models.DecimalField(max_digits=12, decimal_places=2)
    key = models.CharField(max_length=45, verbose_name='API ID', unique=True, null=False)

    def __str__(self) -> str:
        return f"{self.name} - {self.price}"