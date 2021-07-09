from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth import get_user_model


# Create your models here.
class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    title = models.CharField(max_length=200, verbose_name='Title')
    author = models.CharField(max_length=200, verbose_name='Author')
    description = models.TextField(
        max_length=650, verbose_name='Description', blank=True)
    price = models.DecimalField(
        decimal_places=2, max_digits=6, verbose_name='Price')
    cover = models.ImageField(upload_to='covers/', blank=True)

    class Meta:
        verbose_name_plural = 'Books'

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse("book-detail", args=[str(self.id)])


class Review(models.Model):
    book = models.ForeignKey("Book", verbose_name='Book',
                             on_delete=models.CASCADE, related_name='reviews')
    review = models.CharField(max_length=255, verbose_name='Review')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return self.review
