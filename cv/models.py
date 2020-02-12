from django.db import models


class BasicInformation(models.Model):
    order = models.IntegerField()
    typename = models.CharField(max_length=30)
    info = models.TextField()

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.typename


class Experience(models.Model):
    order = models.IntegerField()
    sector = models.CharField(max_length=20, blank=True, default="")
    type = models.CharField(max_length=20)
    time = models.CharField(max_length=20, blank=True, default="")
    period = models.CharField(max_length=20, blank=True, default="")
    event = models.CharField(max_length=30, blank=True, default="")
    title = models.CharField(max_length=40, blank=True, default="")
    subtitle = models.CharField(max_length=40, blank=True, default="")
    detail = models.TextField(blank=True, default="")

    class Meta:
        ordering = ('type', 'order',)

    def __str__(self):
        return self.title
