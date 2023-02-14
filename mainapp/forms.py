from django import forms
from mainapp import models as mainapp_models

class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    item = forms.ChoiceField(choices=tuple(mainapp_models.Item.objects.values_list('key', 'name')))


class ItemForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
  