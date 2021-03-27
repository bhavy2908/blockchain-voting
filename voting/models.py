from django.db import models


class Hash(models.Model):
    prev = models.CharField(max_length=100)
    trans = models.CharField(max_length=100)
    new = models.CharField(max_length=100)
    voter = models.CharField(max_length=100)

    def __str__(self):
        return self.voter
