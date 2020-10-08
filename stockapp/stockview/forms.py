from django import forms
from .models import stocks

class StockForm(forms.ModelForm):
    class Meta: 
        model = stocks 
        fields = ["ticker"]