# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.shortcuts import get_object_or_404


class QuestCategory(models.Model):
    name = models.CharField('имя категории вопроса',max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField('активен?', default=True)
    created = models.DateTimeField(auto_now_add=True , auto_now=False)
    updated = models.DateTimeField(auto_now_add=False , auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'категория вопросов'
        verbose_name_plural = 'категории вопросов'


class Quest(models.Model):
    title = models.TextField('заголовок вопроса', blank=True, null=True, default=None)
    category = models.ForeignKey(QuestCategory, on_delete=models.SET_DEFAULT, max_length=128, blank=True, null=True, default=None, verbose_name='категория вопроса')
    image = models.ImageField('рисунок для вопроса',upload_to='quest_images/', blank=True)
    is_active = models.BooleanField('активен?',default=True)
    created = models.DateTimeField(auto_now_add=True , auto_now=False)
    updated = models.DateTimeField(auto_now_add=False , auto_now=True)

    def __str__(self):
        return "%s" % self.title

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'


class Answer(models.Model):
    quest_f = models.ForeignKey(Quest, on_delete=models.CASCADE, blank=True, null=True, default=None)
    answer_text = models.TextField(verbose_name="текст ответа", default="", blank=True, null=True)
    right = models.BooleanField('верный?',default=False)
    created = models.DateTimeField(auto_now_add=True , auto_now=False)
    updated = models.DateTimeField(auto_now_add=False , auto_now=True)

    def __str__(self):
        return "%s" % self.answer_text

    class Meta:
        verbose_name = 'вариант ответа'
        verbose_name_plural = 'варианты ответов'


class Poll(models.Model):
    time_limit = models.PositiveIntegerField(verbose_name="время на тест. мин", default=5)
    qwests_qty_total = models.PositiveIntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'тест'
        verbose_name_plural = 'тесты'

    def __str__(self):
        return "Опрос № %s" % (self.id)

    def __init__(self,  *args, **kwargs):
        super(Poll, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.id:
            ss = PollItemList.objects.filter(poll = self)
            s_val = 0
            for s in ss:
                s_val += s.quest_capacity_item_list_total
            self.qwests_qty_total = s_val
        super(Poll, self).save(*args, **kwargs)


def get_quest_category_type_choices():
    CAT_TYPE_CHOICES = [(str(e.name), e.name) for e in QuestCategory.objects.all()]
    # CAT_TYPE_CHOICES = []
    # loc_qty_quest = get_object_or_404(QuestCategory, name=self.quest_category_type)
    # for e in QuestCategory.objects.all():
    #     # list = []
    #     loc_quests_local = Quest.objects.filter(category = e.id)
    #     k = e.name
    #     v = e.name + loc_quests_local.id
    #     # dict.update({k: v})
    #     CAT_TYPE_CHOICES.append([k,v])
    #     # CAT_TYPE_CHOICES.append(dict)
    # print(CAT_TYPE_CHOICES)
    return CAT_TYPE_CHOICES
#
# def get_quest_category_type_default():
#     def_value = QuestCategory.objects.filter().first()
#     default = def_value
#     return default

# def get_max_qty_quest_category(value):
#     def_value = QuestCategory.objects.filter().first()
#     default = str(def_value)
#     return default

class PollItemList(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.SET_DEFAULT, max_length=128, blank=True, null=True, default=None)
    quest_category_type = models.CharField(verbose_name="категории вопросов", max_length=256, choices=get_quest_category_type_choices())
    # quest_category_type = models.CharField(verbose_name="категории вопросов", max_length=64, choices=[], default="")
    quest_capacity_item_list_procent = models.PositiveIntegerField(verbose_name="Кол-во вопросов. %", default=100,validators=[MaxValueValidator(100), MinValueValidator(1)])
    quest_capacity_item_list_total = models.PositiveIntegerField(verbose_name="текущее кол-во вопросов", default=0)
    # is_emailed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''

    def __str__(self):
        return "Item List № %s" % (self.id)

    def __init__(self,  *args, **kwargs):
        # int_qty = get_max_qty_quest_category(self.poll.)
        # self._meta.get_field('quest_capacity').validators = [MaxValueValidator(100), MinValueValidator(1)]
        super(PollItemList, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        quest_cat = get_object_or_404(QuestCategory, name=self.quest_category_type)
        quests_local = Quest.objects.filter(category = quest_cat).count()
        self.quest_capacity_item_list_total = quests_local
        super(PollItemList, self).save(*args, **kwargs)


# class PollImage(models.Model):
#     order_fk = models.ForeignKey(Poll, on_delete=models.CASCADE, blank=True, null=True, default=None, verbose_name='Ордер')
#     order_image = models.ImageField('схема помещения', blank=True, null=True, max_length=250)
#     fullpdf_url_staff = models.URLField(max_length=250, blank=True, null=False)
#     created = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True)
#
#     def __str__(self):
#         return "%s" % self.order_image
#
#     class Meta:
#         verbose_name = 'схема помещения'
#         verbose_name_plural = 'схемы помещений'
