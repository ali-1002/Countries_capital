from django.core.validators import MaxValueValidator
from django.db import models

class CapitalModel(models.Model):
    capital_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.capital_name}"

class CountriesModel(models.Model):
    country_name = models.CharField(max_length=50)
    country_population = models.PositiveIntegerField(validators=[MaxValueValidator(2_000_000_000)])
    capital_name = models.OneToOneField(CapitalModel, on_delete=models.CASCADE, unique=True, null=False, blank=False, default='.')
    capital_population = models.PositiveIntegerField(validators=[MaxValueValidator(100_000_000)])
    country_flag_photos = models.ImageField(upload_to='flag_photos', default='default_flag/img.png', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.country_name}"

    class Meta:
        db_table = 'countries'