from django.contrib import admin
from .models import *
from smena_tests.models import Quest, Answer
import nested_admin
from django.conf import settings

# Register your models here.
# class PolledItemListInline(admin.TabularInline):
#     model = PolledItemList
#     readonly_fields = [field.name for field in PolledItemList._meta.fields]

# class PolledAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Polled._meta.fields]
#     inlines = [PolledItemListInline]
# admin.site.register(Polled, PolledAdmin)



class PolledItemListAnswersInline(nested_admin.NestedTabularInline):
    readonly_fields = [field.name for field in PolledItemListAnswers._meta.fields]
    model = PolledItemListAnswers
    extra = 0

class PolledItemListInline(nested_admin.NestedTabularInline):
    model = PolledItemList
    inlines = [PolledItemListAnswersInline,]
    readonly_fields = [field.name for field in PolledItemList._meta.fields]
    extra = 0

class PolledAdmin(nested_admin.NestedModelAdmin):
    class Media:
        # js = ('js/admin/jquery.js','js/admin/my_own_admin.js',)
        js = ('js/admin/jquery.js',)
        css = {
             'all': ('css/admin/my_own_admin.css',)
        }
    list_display = [field.name for field in Polled._meta.fields]

    # list_display = [field.name for field in Polled._meta.fields]
    inlines = [PolledItemListInline,]

admin.site.register(Polled, PolledAdmin)

class PolledItemListAnswersAdmin(nested_admin.NestedModelAdmin):
    # list_display = [field.name for field in PolledItemListAnswers._meta.fields]
    readonly_fields = [field.name for field in PolledItemListAnswers._meta.fields]
admin.site.register(PolledItemListAnswers, PolledItemListAnswersAdmin)




    # fields = ('polled', 'quest',)

    # list_display = [field.name for field in Poll._meta.fields]
