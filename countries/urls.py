from django.urls import path
from .views import home_view, country_view, country_delete_view, add_country_view, add_capital_view

urlpatterns = [
    path('', home_view, name='home'),
    path('countries/<int:id>/', country_view, name='countries'),
    path('countries/delete/<int:id>', country_delete_view, name='country_delete'),
    path('countries/add/', add_country_view, name='add_country'),
    path('capital/add/', add_capital_view, name='add_capital'),
]