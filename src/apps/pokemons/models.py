from django.db import models
from django_prometheus.models import ExportModelOperationsMixin
from django.contrib.auth import get_user_model


User = get_user_model()


class Pokeball(models.Model):
    name = models.CharField('Pokeball name', max_length=32)
    level = models.PositiveIntegerField(
        'How match attempt for getting the Pokemon')


class Pokemon(ExportModelOperationsMixin('pokemon'), models.Model):
    """ Pokemon Model """
    name = models.CharField('Pokemon name', max_length=120)
    level = models.PositiveIntegerField('Level')
    pokeball = models.ForeignKey(Pokeball, on_delete=models.CASCADE, verbose_name='In which pokeball')
    master = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Pokemon Master')
