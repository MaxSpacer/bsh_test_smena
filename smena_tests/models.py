# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.shortcuts import get_object_or_404
# from django import forms
# from django.forms import HiddenInput


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
    name_poll = models.CharField('Имя теста',max_length=64, blank=True, null=True, default=None)
    time_limit = models.PositiveIntegerField(verbose_name="время на тест. мин", default=5)
    qwests_qty_total = models.PositiveIntegerField(verbose_name="всего вопросов в тесте", null=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'тест'
        verbose_name_plural = 'тесты'

    def __str__(self):
        return "Тест № %s" % (self.id)

    def __init__(self,  *args, **kwargs):
        super(Poll, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        # if self.id:
        #     ss = PollItemList.objects.filter(poll = self)
        #     s_val = 0
        #     for s in ss:
        #         s_val += s.quest_capacity_item_list_total
        #     self.qwests_qty_total = s_val
        super(Poll, self).save(*args, **kwargs)


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
    # quest_category_type = models.ForeignKey(QuestCategory, verbose_name="категории вопросов", on_delete=models.SET_DEFAULT, max_length=128, blank=True, null=True, default=None)
    quest_category_type = models.CharField(verbose_name="категории вопросов", max_length=128, choices=None)
    # quest_category_title = models.CharField(max_length=128, blank=True, null=True, default=None)
    quest_category_title = models.CharField(max_length=128)
    # quest_category_type = models.CharField(verbose_name="категории вопросов", max_length=64, choices=[], default="")
    quest_capacity_item_list_procent = models.PositiveIntegerField(verbose_name="Кол-во вопросов. %", default=100, validators=[MaxValueValidator(100), MinValueValidator(1)])
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
        def get_quest_category_type_choices():
            CAT_TYPE_CHOICES = []
            pp = QuestCategory.objects.all()
            print(pp)
            for e in pp:
                y = e.name
                x = Quest.objects.filter(category=e).count()
                list = []
                list = [str(x),y]
                CAT_TYPE_CHOICES.append(list)
            return CAT_TYPE_CHOICES
        self._meta.get_field('quest_category_type').choices = get_quest_category_type_choices()
        # self._meta.get_field('quest_category_title').widget = forms.HiddenInput()
        # self._meta.get_field('quest_category_title').attrs={'type' : 'hidden'})
        super(PollItemList, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        # qu =  PollItemList.objects.filter(poll=self.poll)
        # n = 0
        # n += self.quest_capacity_item_list_total
        # print('n')
        # print(n)
        # for quu in qu:
        #     n += quu.quest_capacity_item_list_total
        #
        # po = get_object_or_404(Poll, id=self.poll.id)
        # po.polled_qty_quests = n
        # print('n+')
        # print(n)
        # po.save
        # quests_local = Quest.objects.filter(category = quest_cat).count()
        # self.quest_capacity_item_list_total = quests_local
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
