# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


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
    title = models.CharField('заголовок вопроса', max_length=128, blank=True, null=True, default=None)
    category = models.ForeignKey(QuestCategory, on_delete=models.SET_DEFAULT, max_length=128, blank=True, null=True, default=None, verbose_name='категория вопроса')
    image = models.ImageField('рисунок для вопроса',upload_to='quest_images/')
    # weight = models.IntegerField('вес',default=0)
    # description = models.TextField('описание', blank=True, null=True, default=None)
    # popular = models.BooleanField('популярные товары', default=False)
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
    # answer_text = models.CharField(verbose_name="текст ответа", default="", max_length=64, blank=False, null=True)
    right = models.BooleanField('верный?',default=False)
    created = models.DateTimeField(auto_now_add=True , auto_now=False)
    updated = models.DateTimeField(auto_now_add=False , auto_now=True)

    def __str__(self):
        return "%s" % self.image

    class Meta:
        verbose_name = 'вариант ответа'
        verbose_name_plural = 'варианты ответов'


class Poll(models.Model):
    # poll_number = models.PositiveIntegerField(blank=True, null=True, default = 0)
    is_emailed = models.BooleanField(default=False)
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
        super(Poll, self).save(*args, **kwargs)


def get_quest_category_type_choices():
    CAT_TYPE_CHOICES = [(str(e.docs_type), e.docs_type) for e in QuestCategory.objects.all()]
    return CAT_TYPE_CHOICES
#
def get_quest_category_type_default():
    def_value = QuestCategory.objects.filter().first()
    default = str(def_value)
    return default

# def get_max_qty_quest_category(value):
#     def_value = QuestCategory.objects.filter().first()
#     default = str(def_value)
#     return default

class PollItemList(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.SET_DEFAULT, max_length=128, blank=True, null=True, default=None)
    # quest_category_type = models.CharField(verbose_name="Тип документа", max_length=64, choices=get_quest_category_type_choices(), default=get_quest_category_type_default())
    quest_category_type = models.CharField(verbose_name="категория вопросов", max_length=64, choices=[], default="")
    quest_capacity = models.PositiveIntegerField(default=1,validators=[MaxValueValidator(100), MinValueValidator(1)])
    is_emailed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''

    def __str__(self):
        return "Опрос № %s %s" % (self.id, self.poll_number)

    def __init__(self,  *args, **kwargs):
        # int_qty = get_max_qty_quest_category(self.poll.)
        self._meta.get_field('quest_capacity').validators = [MaxValueValidator(100), MinValueValidator(1)]
        super(PollItemList, self).__init__(*args, **kwargs)





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
