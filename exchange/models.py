from django.db import models


class ExchangeProgram(models.Model):
    university = models.CharField(max_length=255)
    languages = models.CharField(max_length=255)
    seats = models.CharField(max_length=50)
    deadline = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.university