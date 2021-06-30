from django.db import models
from django.urls import reverse
import uuid


# Create your models here.
class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    title = models.CharField(max_length=200, verbose_name='Title')
    author = models.CharField(max_length=200, verbose_name='Author')
    price = models.DecimalField(
        decimal_places=2, max_digits=6, verbose_name='Price')

    class Meta:
        verbose_name_plural = 'Books'

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse("book-detail", args=[str(self.id)])
