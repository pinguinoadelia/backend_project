from django.db import models
from django.contrib.auth.models import User

class Reparto(models.Model):
    # definisco i tre reparti
    ELETTRONICA = 'elettronica'
    BELLEZZA    = 'bellezza'
    LIBRI       = 'libri'
    REPARTI_CHOICES = [
        (ELETTRONICA, 'Elettronica'),
        (BELLEZZA,    'Bellezza'),
        (LIBRI,       'Libri'),
    ]

    nome = models.CharField(
        max_length=20,
        choices=REPARTI_CHOICES,
        unique=True,
        verbose_name='Reparto'
    )
    managers = models.ManyToManyField(
        User,
        blank=True,
        verbose_name='Office Managers assegnati',
        limit_choices_to={'groups__name': 'Office Managers'},
        related_name='reparti_ufficio'
    )

    class Meta:
        verbose_name = 'Reparto'
        verbose_name_plural = 'Reparti'

    def __str__(self):
        # restituisce la label leggibile
        return dict(self.REPARTI_CHOICES)[self.nome]
