from django.shortcuts import render
from django.forms import modelformset_factory, Textarea
from .models import Polled, PolledItemList, PolledItemListAnswers
from smena_tests.models import Poll, PollItemList, Quest, QuestCategory, Answer
from django.shortcuts import get_object_or_404
from .forms import PolledItemListAnswersForm
from django.shortcuts import redirect
from django.views.generic.edit import UpdateView
import datetime
from django.urls import reverse_lazy
from django.utils import timezone
from django.http import JsonResponse


def polledlistview(request):
    if request.user.is_authenticated:
        user = request.user
        context = Polled.objects.filter(polled_user=user).order_by('-id')
        return render(request, 'polled/polled_list.html', {'polled':context})
    else:
        return redirect('/accounts/login/')


def polled_itog(request, pk):
    polled = get_object_or_404(Polled, pk=pk)
    return render(request, 'polled/test_done.html', {'polled': polled})


def quest_formset_render(request, pk):
    print('polled_pk-----')
    print(pk)
    if request.user.is_authenticated:
        polled = get_object_or_404(Polled, pk=pk)
        if datetime.datetime.now(tz=timezone.utc) < polled.finish_date and polled.is_done == False:
            QuestFormSet = modelformset_factory(PolledItemListAnswers, extra=0, form=PolledItemListAnswersForm)
            if request.method == "POST":
                form = QuestFormSet(request.POST)
                instance = form.save()
                j = form[0].instance.polled
                print('j')
                print(j.polled.polled_poll)
                total_right_answers = 0
                total_wrong_answers = 0
                total_answers = 0
                for pila in form:
                    total_answers += 1
                    if pila.instance.is_right and pila.instance.is_selected:
                        total_right_answers += 1
                    elif not pila.instance.is_right and not pila.instance.is_selected:
                        total_right_answers += 1
                    elif pila.instance.is_right and not pila.instance.is_selected:
                        total_wrong_answers += 1
                    elif not pila.instance.is_right and pila.instance.is_selected:
                        total_wrong_answers += 1
                print('total_answers----')
                print(total_answers)
                j.qty_rights_answers = total_right_answers
                j.qty_wrong_answers = total_wrong_answers
                j.is_answered = True
                perc = round((total_right_answers/total_answers)*100)
                j.polled_item_list_bal_procent = perc
                totals_pil = PolledItemList.objects.filter(polled=polled).count()
                print('totals_pil')
                print(totals_pil)
                for inst_pila in instance:
                    inst_pila.local_price = 100/len(instance)
                    ccc = (100/totals_pil)
                    inst_pila.global_price = ccc/len(instance)
                    inst_pila.save()
                j.save()
            d = PolledItemList.objects.filter(polled=polled, is_answered = False).order_by("?").first()
            if d:
                print('generim cherez form')
                print(d)
                formset = QuestFormSet(queryset=PolledItemListAnswers.objects.filter(polled=d.id).order_by("?"))
                quest_image = d.quest.image
                quest = d.quest
                if not quest_image:
                    quest_image = None
                time_for_js_countdown = polled.finish_date
                polled_for_context = polled
                ppi = polled.polled_poll.id
                ppn = polled.polled_poll.name_poll
                poll_for_context = 'к тесту № ' + str(ppi) + ':' +  str(ppn)
                return render(request, 'polled/create_test_new.html', {
                'formset': formset,
                'quest_image':quest_image,
                'quest':quest,
                'polled_for_context':polled_for_context,
                'poll_for_context':poll_for_context,
                 'time_for_js_countdown':time_for_js_countdown
                 })
            else:
                polled.is_done = True
                print('======test')
                print(polled.polled_total_perc)
                polled.save()
                return redirect(reverse_lazy('polled:polled_itog_n', kwargs={'pk': polled.id}))
        else:
            polled.is_done = True
            print('======test2')
            print(polled.polled_total_perc)
            polled.save()
            return redirect(reverse_lazy('polled:polled_itog_n', kwargs={'pk': polled.id}))
    else:
        return redirect('/accounts/login/')


def create_polled_order(request, pk):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    if request.user.is_authenticated:
        poll = get_object_or_404(Poll, id=pk, is_active=True)
        user = request.user
        polled_user = Polled.objects.filter(polled_user=user, is_done=False)
        if polled_user:
            for pol in polled_user:
                pol.is_done = True
                pol.save()
        else:
            pass
        if poll:
            pool_quests = []
            poll_items_list = PollItemList.objects.filter(poll=poll)
            for x in poll_items_list:
                # print('x.quest_category_type')
                print(x.quest_category_title)
                quest_category = get_object_or_404(QuestCategory, name = x.quest_category_title)
                quest_items_list_by_category = Quest.objects.filter(category=quest_category)
                qty_quests = quest_items_list_by_category.count()
                quest_capacity = x.quest_capacity_item_list_total
                # percent_quest_capacity = x.quest_capacity_item_list_procent
                # percented_qty = round(qty_quests/100*percent_quest_capacity)
                # if percented_qty == 0:
                #     percented_qty = 1
                # print("Общее кол-во квестов в каждой категории: {qq}\nПроцент который будем юзать из этого кол-ва:{pre} \nКол-во посчитанных квестов:{per}".format(qq=qty_quests,pre=percent_quest_capacity,per=percented_qty))
                # print('----------quest_items_list_by_category--------')
                # print(quest_items_list_by_category)
                # print('----------select_random_quests-----------')
                select_random_quests = quest_items_list_by_category.order_by('?')[:quest_capacity]
                print(select_random_quests)
                for x in select_random_quests:
                    pool_quests.append(x)
            print('-----pool_quests------')
            print(pool_quests)
            print(len(pool_quests))
            print('poll_items_list')
            print(poll_items_list)
            l = int(poll.time_limit)
            finish_date = datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(minutes=l)
            obj, created = Polled.objects.get_or_create(polled_poll=poll,polled_user=request.user, polled_qty_quests=len(pool_quests), time_lim=l, finish_date=finish_date, is_init=True)
            if created:
                for d in pool_quests:
                    pil = PolledItemList(polled=obj,quest=d)
                    pil.save()
                    answers = Answer.objects.filter(quest_f=d)
                    for b in answers:
                        bool = False
                        if b.right:
                            bool = True
                        ans = PolledItemListAnswers(polled=pil, polled_answer=b, is_right = bool)
                        ans.save()
                print("created")
            print('genim first')
            if obj:
                return redirect(reverse_lazy('polled:quest_formset_render_n', kwargs={'pk': obj.id}))
            else:
                return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/accounts/login/')
