from django import forms
from .models import Category, Donation, Institution, User
from django.contrib.auth.forms import AuthenticationForm


def number_validator(number):
    if not number > 0:
        raise forms.ValidationError("Liczba worków musi być dodatnia!")


class DonationForm(forms.Form):
    category = forms.ModelMultipleChoiceField(queryset=Category.objects)
    quantity = forms.IntegerField(min_value=1, validators=[number_validator])
    institution = forms.ModelChoiceField(queryset=Institution.objects)
    address = forms.CharField(max_length=60)
    phone_number = forms.IntegerField()
    city = forms.CharField(max_length=30)
    zip_code = forms.IntegerField()
    pick_up_date = forms.DateField()
    pick_up_time = forms.TimeField()
    pick_up_comment = forms.CharField(max_length=200)


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'password',
                  "repeat_password"
                  ]
        widgets = {
            'password': forms.PasswordInput
        }
    repeat_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        repeat_password = cleaned_data.get('repeat_password')

        if password != repeat_password:
            msg = "Upewnij się że hasła są takie same!"
            self.add_error('password', msg)
            self.add_error('repeat_password', msg)
