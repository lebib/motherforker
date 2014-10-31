from django.conf import settings
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


from .base import NamedDescribed, NULLABLE


class Type(NamedDescribed, MPTTModel):
    parent = TreeForeignKey('self', related_name='children', **NULLABLE)

    class MPTTMeta:
        order_insertion_by = ['name']


class Entity(NamedDescribed, MPTTModel):
    parent = TreeForeignKey('self', related_name='children', **NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, **NULLABLE)
    type = models.ForeignKey(Type, **NULLABLE)

    class MPTTMeta:
        order_insertion_by = ['name']
