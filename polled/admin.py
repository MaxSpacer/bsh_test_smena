from django.contrib import admin
from .models import *
# Register your models here.
class PolledItemListInline(admin.TabularInline):
    model = PolledItemList
    # fields = ('polled', 'quest',)
    readonly_fields = [field.name for field in PolledItemList._meta.fields]

    # list_display = [field.name for field in Poll._meta.fields]


class PolledAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Polled._meta.fields]
    inlines = [PolledItemListInline]
admin.site.register(Polled, PolledAdmin)
