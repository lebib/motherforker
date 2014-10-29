from django.conf import settings
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


NULLABLE = {"blank": True, "null": True}


class Location(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', related_name='children',
                            **NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             **NULLABLE)

    class MPTTMeta:
        order_insertion_by = ['name']


class Type(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(**NULLABLE)
    parent = TreeForeignKey('self', related_name='children',
                            **NULLABLE)

    class MPTTMeta:
        order_insertion_by = ['name']


class Item(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(**NULLABLE)
    location = models.ForeignKey(Location,
                                 **NULLABLE)
    type = models.ForeignKey(Type,
                             **NULLABLE)
    quantity = models.PositiveSmallIntegerField(default=1)
