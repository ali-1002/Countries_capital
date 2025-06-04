from django.contrib import admin
from .models import CountriesModel, CapitalModel

class CountriesModelAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "capital_name":
            kwargs["queryset"] = CapitalModel.objects.filter(countriesmodel__isnull=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(CapitalModel)
admin.site.register(CountriesModel, CountriesModelAdmin)