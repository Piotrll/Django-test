from django import forms
from django.forms import SelectDateWidget

from .models import Expense, Date


class ExpenseSearchForm(forms.Form):
    name = forms.CharField(max_length=50)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False


class DateSearchForm(forms.Form):
    date1 = forms.DateField(input_formats='%Y-%m-%d', widget=SelectDateWidget(years=range(1999, 2100)))
    date2 = forms.DateField(input_formats='%Y-%m-%d', widget=SelectDateWidget(years=range(1999, 2100)))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date1'].required = False
        self.fields['date2'].required = False
