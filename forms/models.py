from django.contrib.auth.models import User
from django.db import models


class FormModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)


class FormField(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    label = models.CharField(max_length=200)
    type = models.CharField(max_length=200, default='text')
    form = models.ForeignKey(FormModel, on_delete=models.CASCADE)


class FormData(models.Model):
    id = models.IntegerField(primary_key=True)
    form_id = models.IntegerField()
    field_id = models.IntegerField()
    value = models.CharField(max_length=200)
    record_id = models.IntegerField()


class FormRecord(models.Model):
    date = models.DateTimeField()
