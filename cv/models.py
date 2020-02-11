from django.db import models


class BasicInformation(models.Model):
    order = models.IntegerField()
    typename = models.CharField(max_length=30)
    info = models.TextField()

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.typename


class Education(models.Model):
    order = models.IntegerField()
    time = models.CharField(max_length=20)
    period = models.CharField(max_length=20)
    school = models.CharField(max_length=30)
    major = models.CharField(max_length=40)
    college = models.CharField(max_length=40)
    detail = models.TextField()

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.period
