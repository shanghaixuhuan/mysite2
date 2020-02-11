from django.db import models


class BasicInformation(models.Model):
    order = models.IntegerField()
    typename = models.CharField(max_length=30)
    info = models.CharField(max_length=300)

    class Meta:
        ordering = ('-order',)

    def __str__(self):
        return self.typename