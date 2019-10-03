from django.shortcuts import render
from django.forms import modelformset_factory, Textarea
from .models import Polled, PolledItemList, PolledItemListAnswers
from smena_tests.models import Poll, PollItemList, Quest, QuestCategory, Answer
from django.shortcuts import get_object_or_404
from .forms import PolledItemListAnswersForm
# from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic.edit import UpdateView
import datetime
from django.urls import reverse_lazy
from django.utils import timezone


def quest_formset_render(request, pk):
    print('polled_pk-----')
    print(pk)
    if request.user.is_authenticated:
        polled = get_object_or_404(Polled, pk=pk)
        if datetime.datetime.now(tz=timezone.utc) < polled.finish_date and polled.is_done == False:
            QuestFormSet = modelformset_factory(PolledItemListAnswers, extra=0, form=PolledItemListAnswersForm)
            # QuestFormSet = modelformset_factory(PolledItemListAnswers, fields=("polled_answer" ,'is_selected'), extra=0)
            if request.method == "POST":
                form = QuestFormSet(request.POST)
                instance = form.save()
                j = form[0].instance.polled
                # jj = j.instance.polled
                print('============= j ============')
                print(j)
                print(type(j))

                # polled_item_list_answers = PolledItemListAnswers.objects.filter(polled=pk, polled__is_answered = False)
                total_right_answers = 0
                total_wrong_answers = 0
                for pila in form:
                    if pila.instance.is_right and pila.instance.is_selected:
                        total_right_answers += 1
                    elif not pila.instance.is_right and pila.instance.is_selected:
                        total_wrong_answers += 1

                j.qty_rights_answers = total_right_answers
                j.qty_wrong_answers = total_wrong_answers
                j.is_answered = True
                j.save()

            d = PolledItemList.objects.filter(polled=polled, is_answered = False).order_by("?").first()
            if d:
                print('generim cherez form')
                print(d)
                formset = QuestFormSet(queryset=PolledItemListAnswers.objects.filter(polled=d.id))

                # quest = Quest.objects.filter(polleditemlist__id=d.id))
                quest_image = d.quest.image
                if not quest_image:
                    quest_image = None
                return render(request, 'polled/create_test_new.html', {'formset': formset, 'quest_image':quest_image})
            else:
                polled.is_done = True
                polled.save()
                return render(request, 'polled/test_done.html')
        else:
            polled.is_done = True
            polled.save()
            return render(request, 'polled/test_done.html')
    else:
        return redirect('/accounts/login/')


def create_polled_order(request, pk):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    if request.user.is_authenticated:
        poll = get_object_or_404(Poll, id=pk, is_active=True)
        if poll:
            pool_quests = []
            poll_items_list = PollItemList.objects.filter(poll=poll)
            for x in poll_items_list:
                quest_category = get_object_or_404(QuestCategory, name = x.quest_category_type)
                quest_items_list_by_category = Quest.objects.filter(category=quest_category)
                qty_quests = quest_items_list_by_category.count()
                percent_quest_capacity = x.quest_capacity_item_list_procent
                percented_qty = round(qty_quests/100*percent_quest_capacity)
                if percented_qty == 0:
                    percented_qty = 1
                print("Общее кол-во квестов в каждой категории: {qq}\nПроцент который будем юзать из этого кол-ва:{pre} \nКол-во посчитанных квестов:{per}".format(qq=qty_quests,pre=percent_quest_capacity,per=percented_qty))
                print('----------quest_items_list_by_category--------')
                print(quest_items_list_by_category)
                print('----------select_random_quests-----------')
                select_random_quests = quest_items_list_by_category.order_by('?')[:percented_qty]
                print(select_random_quests)
                for x in select_random_quests:
                    pool_quests.append(x)

            print('-----pool_quests------')
            print(pool_quests)
            print(len(pool_quests))

            print('poll_items_list')
            print(poll_items_list)
            obj, created = Polled.objects.get_or_create(polled_poll=poll,polled_user=request.user, polled_qty_quests=len(pool_quests), time_lim=poll.time_limit, is_init=True)
            if created:
                for d in pool_quests:
                    pil = PolledItemList(polled=obj,quest=d)
                    pil.save()
                    answers = Answer.objects.filter(quest_f=d)
                    # print(answers)
                    for b in answers:
                        bool = False
                        if b.right:
                            bool = True
                        ans = PolledItemListAnswers(polled=pil, polled_answer=b, is_right = bool)
                        ans.save()
                print("created")
            # print('request-2')
            # print(request)
            # dpil = PolledItemList.objects.filter(polled=obj, is_answered = False).order_by("?").first()
            print('genim first')
            # print(dpil)
            if obj:
                return redirect(reverse_lazy('polled:quest_formset_render_n', kwargs={'pk': obj.id}))

                # return quest_formset_render(request, dpil.id)
            else:
                return redirect('/')
    else:
        return redirect('/accounts/login/')
        # return print('no  auth')
