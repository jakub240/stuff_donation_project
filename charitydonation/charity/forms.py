from django import forms
from .models import Category, Donation, Institution
from django.contrib.auth.forms import AuthenticationForm


def number_validator(number):
    if not number > 0:
        raise forms.ValidationError("Liczba worków musi być dodatnia!")


class DonationForm(forms.Form):
    category = forms.ModelMultipleChoiceField(queryset=Category.objects)
    quantity = forms.IntegerField(min_value=1, validators=[number_validator])
    institution = forms.ModelChoiceField(queryset=Institution.objects)
