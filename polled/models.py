from django.db import models
from smena_tests.models import Poll, Quest
from django.contrib.auth.models import User

# Create your models here.
class Polled(models.Model):
    polled_poll = models.ForeignKey(Poll, on_delete=models.SET_DEFAULT, max_length=128, blank=True, null=True, default=None)
    polled_user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, max_length=128, blank=True, null=True, default=None)
    polled_qty_quests = models.PositiveSmallIntegerField('Кол-во вопросов', blank=True, null=True, default = 0)
    # time_limit = models.PositiveIntegerField(verbose_name="время на тест. мин", default=5)
    # qwests_qty_total = models.PositiveIntegerField(blank=True, null=True)
    is_init = models.BooleanField(default=True)
    is_done = models.BooleanField(default=False)
    # created = models.DateTimeField(auto_now_add=True, auto_now=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Пройденый опрос'
        verbose_name_plural = 'Пройденый опросы'

    def __str__(self):
        return "Пройденый опрос № %s" % (self.id)

    def __init__(self,  *args, **kwargs):
        super(Polled, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        # if self.id:
        #     ss = PollItemList.objects.filter(poll = self)
        #     s_val = 0
        #     for s in ss:
        #         s_val += s.quest_capacity_item_list_total
        #     self.qwests_qty_total = s_val
        super(Polled, self).save(*args, **kwargs)

class PolledItemList(models.Model):
    polled = models.ForeignKey(Polled, on_delete=models.CASCADE, max_length=128, blank=True, null=True, default=None)
    quest = models.ForeignKey(Quest, on_delete=models.SET_DEFAULT, max_length=128, blank=True, null=True, default=None)

    # quest_category_type = models.CharField(verbose_name="категории вопросов", max_length=256, choices=get_quest_category_type_choices())
    # quest_category_type = models.CharField(verbose_name="категории вопросов", max_length=64, choices=[], default="")
    # quest_capacity_item_list_procent = models.PositiveIntegerField(verbose_name="Кол-во вопросов. %", default=100,validators=[MaxValueValidator(100), MinValueValidator(1)])
    # quest_capacity_item_list_total = models.PositiveIntegerField(verbose_name="текущее кол-во вопросов", default=0)
    # is_emailed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Polled Item List'
        verbose_name_plural = 'Polled Item Lists'

    def __str__(self):
        return "Polled Item List № %s" % (self.id)

    # def __init__(self,  *args, **kwargs):
        # int_qty = get_max_qty_quest_category(self.poll.)
        # self._meta.get_field('quest_capacity').validators = [MaxValueValidator(100), MinValueValidator(1)]
        # super(PolledItemList, self).__init__(*args, **kwargs)

    # def save(self, *args, **kwargs):
        # quest_cat = get_object_or_404(QuestCategory, name=self.quest_category_type)
        # quests_local = Quest.objects.filter(category = quest_cat).count()
        # self.quest_capacity_item_list_total = quests_local
        # super(PolledItemList, self).save(*args, **kwargs)
