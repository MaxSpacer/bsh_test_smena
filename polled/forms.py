from django import forms
from .models import PolledItemListAnswers
from django.forms import modelformset_factory, CharField, Textarea

class PolledItemListAnswersForm(forms.ModelForm):

    # If you want to set a default.

    extra_field = forms.CharField(label='TextOfCategory')
    # User._meta.get_field('username')
    # If you want to dynamically set a value:

    # def __init__(self, *args, **kwargs):
    #
    #
    #
    #     super(form,self).__init(*args, **kwargs)
    #     self.fields['extra_field'].initial = "harvard"
# widgets = {'extra_field': Textarea(attrs={'cols': 80, 'rows': 20})}



    class Meta:
        model = PolledItemListAnswers
        fields = ('extra_field', 'is_selected')


    def __init__(self, *args, **kwargs):
        super(PolledItemListAnswersForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            # self.fields['polled_answer'].disabled = True
            # hh = self.fields['polled_answer']
            # print(instance.polled_answer)

            # super(form,self).__init(*args, **kwargs)
            # my_projects = self.fields['polled_answer'].queryset.filter(my=True)
            self.fields['extra_field'].initial = str(instance.polled_answer)

            # self.fields['polled_answer'].widgets={'polled_answer': Textarea(attrs={'cols': 80, 'rows': 20})}
