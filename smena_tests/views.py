# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from smena_tests.models import Poll
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView


class HomePageView(LoginRequiredMixin, ListView):

    login_url = 'accounts/login/'
    redirect_field_name = 'redirect_to'
    context_object_name = 'queryset'

    def get_queryset(self):
        return Poll.objects.exclude(polled__is_init = True)
        # return Poll.objects.exclude(polled__is_init = True, polled__polled_user = self.request.user)
