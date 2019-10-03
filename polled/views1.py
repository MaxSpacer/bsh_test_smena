from django.shortcuts import render
from django.forms import modelformset_factory
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

# class AuthorUpdate(UpdateView):
#     model = Author
#     fields = ['name']
def quest_formset_render(request, pk):
    print('polled_item_list_pk-----')
    print(pk)
    if request.user.is_authenticated:
        polled_item_list_obj = get_object_or_404(PolledItemList, pk=pk)
        print('polled_item_list_obj-----')
        print(polled_item_list_obj)
        p = polled_item_list_obj.polled
        polled = get_object_or_404(Polled, pk=polled_item_list_obj.polled.id)
        # import datetime
        if datetime.datetime.now(tz=timezone.utc) < polled.finish_date and polled.is_done == False:
            QuestFormSet = modelformset_factory(PolledItemListAnswers, fields=("polled_answer" ,'is_selected'), extra=0)
            if request.method == "POST":
                form = QuestFormSet(request.POST)
                instance = form.save()
                # polled_item_list = PolledItemList.objects.filter(pk=pk).update(is_answered=True)
                # print('polled_item_list_obj')
                # print(polled_item_list_obj)
                polled_item_list_answers = PolledItemListAnswers.objects.filter(polled=pk, polled__is_answered = False)
                # print('polled_item_list_answers')
                total_right_answers = 0
                total_wrong_answers = 0
                for pila in polled_item_list_answers:
                    if pila.is_right and pila.is_selected:
                        total_right_answers += 1
                        # print('total_right_answer')
                        # print(total_right_answers)
                    elif not pila.is_right and pila.is_selected:
                        total_wrong_answers += 1
                        # print('total_wrong_answers')
                        # print(total_wrong_answers)

                        # print('----------------')
                polled_item_list_obj.qty_rights_answers = total_right_answers
                # print(total_right_answers)
                polled_item_list_obj.qty_wrong_answers = total_wrong_answers
                # print(total_wrong_answers)
                polled_item_list_obj.is_answered = True
                print('polled_item_list_obj-----3')
                print(polled_item_list_obj)
                polled_item_list_obj.save()
                d = PolledItemList.objects.filter(polled=polled, is_answered = False).order_by("?").first()
                if d:
                    print('genom cherez form')
                    print(d)
                    form = QuestFormSet(queryset=PolledItemListAnswers.objects.filter(polled=d.id))
                else:
                    polled.is_done = True
                    polled.save()
                    return redirect('/')
            else:
                form = QuestFormSet(queryset=PolledItemListAnswers.objects.filter(polled=polled_item_list_obj))

                # print('polled_item_list_obj222')
                # print(polled_item_list_obj)
                # polled_item_list_answers_total = PolledItemListAnswers.objects.filter(polled=pk, polled__is_answered = False)
                # print(polled_item_list)
            # form = QuestFormSet(queryset=)
                # return redirect(reverse_lazy('polled:quest_formset_render_n', kwargs={'pk': dpil.id}))

            return render(request, 'polled/create_test_new.html', {'form': form})
            # print('polled_item_list_obj-----3')
            # print(d)

            # print('less')
            # print(polled.is_done)
        else:
            polled.is_done = True
            polled.save()
            return render(request, 'polled/test_done.html')
            # print('more')
            # print(polled.is_done)
            # if  polled.finish_date
        # print('polled')
        # print(polled)

            # polled =
            # pass
            # return render(request, 'polled/create_test_new.html', {'form': form})


        #             if form.is_valid():
        #                 pooled_item = form.save(commit=False)
        #                 pooled_item.polled = obj
        #                 # pooled_item.published_date = timezone.now()
        #                 pooled_item.save()
        #                 return redirect('/')
    else:
        return redirect('/')



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
            dpil = PolledItemList.objects.filter(polled=obj, is_answered = False).order_by("?").first()
            print('genim first')
            print(dpil)
            if dpil:
                return redirect(reverse_lazy('polled:quest_formset_render_n', kwargs={'pk': dpil.id}))

                # return quest_formset_render(request, dpil.id)
            else:
                return redirect('/')
    else:
        return redirect('/accounts/login/')
        # return print('no  auth')
