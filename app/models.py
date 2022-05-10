from django.db import models


class Ai1(models.Model):
    id = models.IntegerField(primary_key=True)
    current = models.FloatField()
    STS_CHOICES = ((1, '1'), (2, '2'))
    sts = models.IntegerField(choices=STS_CHOICES, default=1)


class Ai2(models.Model):
    id = models.IntegerField(primary_key=True)
    current = models.FloatField()
    STS_CHOICES = ((1, '1'), (2, '2'))
    sts = models.IntegerField(choices=STS_CHOICES, default=1)
