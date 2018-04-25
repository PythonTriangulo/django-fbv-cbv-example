from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField('título', max_length=200)
    author = models.CharField('autor', max_length=200)
    year_publication = models.PositiveIntegerField(
        'ano de publicação',
        null=True,
        blank=True
    )
    publisher = models.CharField(
        'editora',
        max_length=100,
        null=True,
        blank=True
    )
    cover = models.URLField('capa', null=True, blank=True)

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:book_detail', kwargs={'pk': self.pk})
