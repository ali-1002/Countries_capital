from django import forms
from .models import CountriesModel, CapitalModel

class CountriesModelForm(forms.ModelForm):
    class Meta:
        model = CountriesModel
        fields = ['country_name', 'country_population', 'capital_name', 'capital_population', 'country_flag_photos']
    
class CapitalModelForm(forms.ModelForm):
    class Meta:
        model = CapitalModel
        fields = ['capital_name']