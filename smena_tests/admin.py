from django.contrib import admin
from .models import *
# Register your models here.


class PollItemListInline(admin.TabularInline):
    model = PollItemList

class PollAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Poll._meta.fields]
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
