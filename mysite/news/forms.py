from .models import Art
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, DateInput, TimeInput, IntegerField, NumberInput
from django import forms

class ArticlesForm(ModelForm):
    class DateInput(forms.DateInput):
        input_type = 'date'

    class Meta:
        model = Art
        fields = ["title", 'anon', 'full', 'vdate', 'vtime', 'table', 'guests']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "anon": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
            "table": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер стола'
            }),
            "guests": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество гостей'
            }),
            "full": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Особые заметки'
            }),
            "vdate": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата',
                'type': 'date'
            }),
            "vtime": TimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Время',
                'type': 'time'
            }),
        }