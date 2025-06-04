from .models import CapitalModel, CountriesModel
from rest_framework import serializers

class CountriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = CountriesModel
        fields = ['country_name', 'country_population', 'capital_name', 'capital_population', 'country_flag_photos']
    
class CapitalSerializers(serializers.ModelSerializer):
    class Meta:
        model = CapitalModel
        fields = ['capital_name']