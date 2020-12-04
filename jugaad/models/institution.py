from django.db import models

class Institution(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    city = models.CharField(max_length=100, blank=False, null=False)
    state = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name
