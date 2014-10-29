from django.conf import settings
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


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


class Location(Named, Described, MPTTModel):
    parent = TreeForeignKey('self', related_name='children',
                            **NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             **NULLABLE)

    class MPTTMeta:
        order_insertion_by = ['name']


class Type(Named, Described, MPTTModel):
    parent = TreeForeignKey('self', related_name='children',
                            **NULLABLE)

    class MPTTMeta:
        order_insertion_by = ['name']


class Item(Named, Described, models.Model):
    location = models.ForeignKey(Location,
                                 **NULLABLE)
    type = models.ForeignKey(Type,
                             **NULLABLE)
    quantity = models.PositiveSmallIntegerField(default=1)
