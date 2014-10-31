from django.db import models


NULLABLE = {"blank": True, "null": True}


class Named(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Described(models.Model):
    description = models.TextField(**NULLABLE)

    class Meta:
        abstract = True


class NamedDescribed(Named, Described):
    class Meta:
        abstract = True
