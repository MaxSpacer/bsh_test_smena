from django.contrib import admin
from .models import *
# Register your models here.
from django.utils.safestring import SafeText

# class PollItemListAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in PollItemList._meta.fields]
# admin.site.register(PollItemList, PollItemListAdmin)

class PollItemListInline(admin.TabularInline):
    model = PollItemList
    fields = [
    'quest_category_type',
    'quest_category_title',
    'quest_capacity_item_list_total',
    ]
    extra = 1


class PollAdmin(admin.ModelAdmin):
    class Media:
        js = (
        'admin/js/vendor/jquery/jquery.min.js',
        'admin/js/jquery.init.js',
        'js/admin/my_own_admin.js',
        )
        css = {
             'all': ('css/admin/my_own_admin.css',)
        }
    def TECT(self, obj):
        return obj
    list_display = [
    'TECT',
    'name_poll',
    'time_limit',
    'qwests_qty_total',
    ]
    # readonly_fields = [
    # 'qwests_qty_total',
    # ]
    inlines = [PollItemListInline]
admin.site.register(Poll, PollAdmin)


class AnswerInline(admin.TabularInline):
    model = Answer

class QuestCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in QuestCategory._meta.fields]
admin.site.register(QuestCategory, QuestCategoryAdmin)

class QuestAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Quest._meta.fields]
    inlines = [AnswerInline]
admin.site.register(Quest, QuestAdmin)
