from django.contrib import admin

from .models import Location, Type, Item


admin.site.register(Location)
admin.site.register(Type)
admin.site.register(Item)
