from django.db import models


class Option(models.Model):
    text = models.TextField(default="Something is here")
