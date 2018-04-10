from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date


# Create your models here.


class Filmes(models.Model):
    nome = models.TextField()
    tipo = models.TextField()
    data_entrega = models.DateField()
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE,)

    def __unicode__(self):
        return u"%s" % self.name


class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True


class FilmeReview(Review):
    filmes = models.ForeignKey(Filmes,on_delete=models.CASCADE)