from django.contrib import admin
from .models import *
from smena_tests.models import Quest, Answer
import nested_admin
from django.conf import settings


class PolledItemListAnswersInline(nested_admin.NestedTabularInline):
    model = PolledItemListAnswers
    verbose_name = "вариант ответов"
    verbose_name_plural = "варианты ответов"
    readonly_fields = [
    'polled_answer',
    'is_right',
    'is_selected',
    'local_price',
    'global_price',
    ]
    extra = 0
    classes = ['collapse']

class PolledItemListInline(nested_admin.NestedTabularInline):
    model = PolledItemList
    verbose_name = "вопрос"
    verbose_name_plural = "вопросы"
    inlines = [PolledItemListAnswersInline,]
    readonly_fields = [
    'quest',
    'polled_item_list_bal_procent',
    'qty_rights_answers',
    'qty_wrong_answers',
    'is_answered',
    ]
    extra = 0
    classes = ['collapse']

class PolledAdmin(nested_admin.NestedModelAdmin):
    class Media:
        js = (
        'admin/js/vendor/jquery/jquery.min.js',
        'admin/js/jquery.init.js',
        'js/admin/my_own_admin.js',
        )
        css = {
             'all': ('css/admin/my_own_admin.css',)
        }
    def get_polled_full_name(self, obj):
        return obj
    def get_poll_full_name(self, obj):
        return obj.polled_poll.name_poll
        # pass
    get_polled_full_name.short_description = 'имя опроса'
    get_poll_full_name.short_description = 'Наименование теста'
    list_display = [
    'get_polled_full_name',
    'get_poll_full_name',
    'polled_poll',
    'polled_user',
    'polled_qty_quests',
    'polled_total_perc',
    'time_lim',
    'created',
    # 'is_done',
    ]
    readonly_fields = [
    'polled_poll',
    'polled_user',
    'polled_qty_quests',
    'polled_total_perc',
    'time_lim',
    'is_done',
    'finish_date',
    ]
    exclude = ['is_init',]
    inlines = [PolledItemListInline,]
    search_fields = ('polled_poll__id', 'polled_user__username', )
admin.site.register(Polled, PolledAdmin)


# class PolledItemListAnswersAdmin(nested_admin.NestedModelAdmin):
#     readonly_fields = [field.name for field in PolledItemListAnswers._meta.fields]
# admin.site.register(PolledItemListAnswers, PolledItemListAnswersAdmin)
