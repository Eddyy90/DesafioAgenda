from typing import ChainMap
from unittest.util import _MAX_LENGTH
from django.db import models


class Contacts(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    idade = models.DecimalField(max_digits=9, decimal_places=0)
    número = models.IntegerField()

    def __str__(self):
        return "%s - %s" % (self.nome, self.email)

    def is_overage(self):
        return self.idade >= 18

class Adresses(models.Model):
    STATE_CHOICES = [
        ('RN', 'Rio Grade do Norte'),
        ('PB', 'Paraiba'),
        ('PE', 'Pernambuco'),
    ]
    state = models.CharField(
        max_length=2,
        choices=STATE_CHOICES,
        default='RN',

    )
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    number = models.IntegerField()
    
    contact = models.ForeignKey(Contacts, on_delete=models.CASCADE)

