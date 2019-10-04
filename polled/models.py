from django.db import models
from smena_tests.models import Poll, Quest, Answer
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
# import datetime

datetime.datetime.now(tz=timezone.utc) # you can use this value
# Create your models here.
class Polled(models.Model):
    polled_poll = models.ForeignKey(Poll, on_delete=models.SET_DEFAULT, max_length=128, blank=True, null=True, default=None)
    polled_user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, max_length=128, blank=True, null=True, default=None)
    polled_qty_quests = models.PositiveSmallIntegerField('Кол-во вопросов', blank=True, null=True, default = 0)
    polled_total_perc = models.PositiveSmallIntegerField(verbose_name="общий бал. %", default=0,validators=[MaxValueValidator(100), MinValueValidator(1)])
    time_lim = models.PositiveIntegerField(verbose_name="время на тест. мин", default=0)
    # qwests_qty_total = models.PositiveIntegerField(blank=True, null=True)
    is_init = models.BooleanField(default=True)
    is_done = models.BooleanField(default=False)
    # created = models.DateTimeField(auto_now_add=True, auto_now=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    finish_date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True, default=None)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Пройденый опрос'
        verbose_name_plural = 'Пройденые опросы'

    def __str__(self):
        return "Пройденый опрос № %s" % (self.id)

    def __init__(self,  *args, **kwargs):
        super(Polled, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        pil = PolledItemList.objects.filter(polled=self)
        if pil:
            qty_pils = pil.count()
            percent_on_quest = 100/qty_pils
            global_total_bal = 0
            for p in pil:
                g = (percent_on_quest/100)*p.polled_item_list_bal_procent
                print(g)
                global_total_bal += g
            self.polled_total_perc = global_total_bal
        super(Polled, self).save(*args, **kwargs)

class PolledItemList(models.Model):
    polled = models.ForeignKey(Polled, on_delete=models.CASCADE, max_length=128, blank=True, null=True, default=None)
    quest = models.ForeignKey(Quest, on_delete=models.SET_DEFAULT, max_length=128, blank=True, null=True, default=None)
    polled_item_list_bal_procent = models.PositiveSmallIntegerField(verbose_name="Бал. %", default=0,validators=[MaxValueValidator(100), MinValueValidator(1)])
    qty_rights_answers = models.PositiveSmallIntegerField('Кол-во правильных ответов', blank=True, null=True, default = 0)
    qty_wrong_answers = models.PositiveSmallIntegerField('Кол-во не правильных ответов', blank=True, null=True, default = 0)
    is_answered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Polled Item List'
        verbose_name_plural = 'Polled Item Lists'

    def __str__(self):
        return "Polled Item List № %s" % (self.id)


class PolledItemListAnswers(models.Model):
    polled = models.ForeignKey(PolledItemList, on_delete=models.CASCADE,blank=True, null=True, default=None)
    polled_answer = models.ForeignKey(Answer, on_delete=models.SET_DEFAULT, blank=True, null=True, default=None)
    is_right = models.BooleanField(default=False)
    is_selected = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Polled Item List Answers'
        verbose_name_plural = 'Polled Item List Answers'

    def __str__(self):
        return "Polled Item List Answers № %s" % (self.id)

    def save(self, *args, **kwargs):
        # print('--------w----------')
        # print(self.polled_answer.answer_text)
        super(PolledItemListAnswers, self).save(*args, **kwargs)
    # self._meta.get_field('quest_capacity').validators = [MaxValueValidator(100), MinValueValidator(1)]
    # super(PolledItemList, self).__init__(*args, **kwargs)

# def save(self, *args, **kwargs):
    # quest_cat = get_object_or_404(QuestCategory, name=self.quest_category_type)
    # quests_local = Quest.objects.filter(category = quest_cat).count()
    # self.quest_capacity_item_list_total = quests_local
    # super(PolledItemList, self).save(*args, **kwargs)
