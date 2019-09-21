from django.shortcuts import render
from .models import Polled, PolledItemList
from smena_tests.models import Poll, PollItemList, Quest, QuestCategory
from django.shortcuts import get_object_or_404
from .forms import PooledItemsForm
# from django.urls import reverse_lazy
from django.shortcuts import redirect


def test_new(request,obj):
    if request.user.is_authenticated:
        print('request')
        print(request)
        if request.method == "POST":
            form = PooledItemsForm(request.POST)
            if form.is_valid():
                pooled_item = form.save(commit=False)
                pooled_item.polled = obj
                # pooled_item.published_date = timezone.now()
                pooled_item.save()
                return redirect('/')
        else:
            form = PooledItemsForm()
            return render(request, 'polled/create_test_new.html', {'form': form})
        # return render(request, 'blog/post_edit.html', {'form': form})
        # form = PooledItemsForm()
        # print('authed')
        # print('obj')
        # # print(obj)
    else:
        print('no  auth')

def create_polled_order(request, pk):
    # education = Education.objects.get(id=pk)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    if request.user.is_authenticated:
        # print('auth')
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
            print('poll_items_list')
            print(poll_items_list)
            obj, created = Polled.objects.get_or_create(polled_poll=poll,polled_user=request.user, polled_qty_quests=len(pool_quests), is_init=True)
            # if created:
                # polled_item_list_object, created = PolledItemList.objects.get_or_create(polled=obj)

            print('request-2')
            print(request)
            return test_new(request,obj)
            # print('created')
            # print(created)
        # Do something for logged-in users.
    else:
        return print('no  auth')
        # Do something for anonymous users.

        # if not request.user.is_authenticated():
        #     return redirect('/')
        # return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        # if not created:
            # print("asd")

    # print(request)
    # return render(request, 'polled/polled.html', locals())
    # return reverse_lazy('polled:test_new_n')
