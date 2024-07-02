from django import forms
from .models import Customer

class DateInput(forms.DateInput):
    input_type = 'date'


class CustomerForms(forms.ModelForm):
    first_name = forms.CharField(label='Nome')
    last_name = forms.CharField()
    email = forms.EmailField()
    birth_date = forms.DateField(widget=DateInput)
    area_code = forms.RegexField(
        regex=r"^\+?1?[0-9]{2}$",
        error_messages={"invalid": 'Número de DDD inválido.'}
    )
    phone_number = forms.RegexField(
        regex=r"^\+?1?[0-9]{9,15}$",
        error_messages={"invalid": 'Número de DDD inválido.'}
    )
    country = forms.CharField()
    state = forms.CharField()
    city = forms.CharField()

    class Meta:
        model = Customer
        fields = (
            'first_name',
            'last_name',
            'email',
            'birth_date',
            'area_code',
            'phone_number',
            'country',
            'state',
            'city',
        )