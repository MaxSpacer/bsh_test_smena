from django import forms
from .models import PolledItemListAnswers
from django.forms import modelformset_factory, CharField, Textarea

class PolledItemListAnswersForm(forms.ModelForm):

    class Meta:
        model = PolledItemListAnswers
        fields = ('polled_answer', 'is_selected')
