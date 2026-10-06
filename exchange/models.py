from django.db import models


class ExchangeProgram(models.Model):
    university = models.CharField(max_length=255)
    country = models.CharField(max_length=100, blank=True, default='')
    languages = models.CharField(max_length=255)
    seats = models.IntegerField(default=0)
    deadline = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.university