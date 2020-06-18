from django.db import models

KIOSKI = (
    ('1', 'Kiosk1'),
    ('2', 'Kiosk2'),
    ('3', 'Kiosk3'),
)


class KioskModel(models.Model):
    kiosk = models.CharField(max_length=120)
    x = models.DecimalField(decimal_places=40, max_digits=45)
    y = models.DecimalField(decimal_places=40, max_digits=45)
    z = models.DecimalField(decimal_places=40, max_digits=45)


STANOWISKA = (
    ('1', 'prawy dolny rog 5e4602ba9184b62beee348c9'),
    ('2', 'A 5e4691cf59f001700ceaf72a'),
    ('3', 'C 5e4691da59f001700ceaf72c'),
)


class TargetPosition(models.Model):
    pozycja = models.CharField(max_length=120, choices=STANOWISKA)


class KioskUser(models.Model):
    name = models.CharField(max_length=120)
    password_api = models.CharField(max_length=120)


PARKINGI = (
    ('1', 'parking-01'),
    ('2', 'parking-02'),
    ('3', 'parking-03'),
    ('4', 'Charger'),
)


class TargetParking(models.Model):
    pozycja = models.CharField(max_length=120, choices=PARKINGI)
