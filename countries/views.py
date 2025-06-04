from django.shortcuts import render, get_object_or_404, redirect
from .models import CountriesModel
from django.db.models import Q
from .forms import CountriesModelForm, CapitalModelForm
from .serializers import CapitalSerializers, CountriesSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def add_country_view(request):
    form = CountriesModelForm()
    if request.method == 'POST':
        form = CountriesModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, template_name="add_country.html", context={
        'form': form
    })

def add_capital_view(request):
    form = CapitalModelForm()
    if request.method == 'POST':
        form = CapitalModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_country')
    
    return render(request, template_name="add_capital.html", context={
        'form': form
    })

def country_delete_view(request, id: int):
    try:
        country_obj = CountriesModel.objects.get(id=id)
        country_obj.delete()

        return redirect('home')

    except CountriesModel.DoesNotExist:
        return redirect('home')

def country_view(request, id: int):
    country_obj = get_object_or_404(CountriesModel, id=id)
    return render(request, template_name='country_view.html', context={
        'countries': country_obj
    })

def home_view(request):

    q = request.GET.get('q')
    countries_objects = CountriesModel.objects.all().order_by("-id")
    if q:
        if q.isdigit():
            countries_objects = CountriesModel.objects.filter(Q(country_population=int(q)))
        else:
            countries_objects = CountriesModel.objects.filter(Q(country_name__icontains=q))
    else:
        countries_objects = CountriesModel.objects.all()
    countries_objects = countries_objects.order_by("-id")
    return render(request, template_name='home.html', context={
        'countries_objects': countries_objects
    })