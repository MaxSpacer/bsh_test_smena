from django import forms
from .models import PolledItemList

class PooledItemsForm(forms.ModelForm):

    class Meta:
        model = PolledItemList
        fields = ('quest',)
