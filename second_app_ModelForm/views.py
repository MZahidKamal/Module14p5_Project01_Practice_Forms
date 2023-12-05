from django.shortcuts import render
from second_app_ModelForm.forms import (SampleModel01_Forms, SampleModel02_Forms, SampleModel03_Forms)

# Create your views here.
def great_devxy_medium(request):
    form01 = sample_model_01_views_function(request)
    form02 = sample_model_02_views_function(request)
    form03 = sample_model_03_views_function(request)
    context = {
        'form01': form01,
        'form02': form02,
        'form03': form03,
    }
    return render(request, 'second_app_ModelForm/great_devxy_medium.html', context)

def sample_model_01_views_function(request):
    if request.method == 'POST':
        sample_model_01_db = SampleModel01_Forms(request.POST)
        if sample_model_01_db.is_valid():
            sample_model_01_db.save(commit=True)
            print(sample_model_01_db.cleaned_data)
    else:
        sample_model_01_db = SampleModel01_Forms()
    return sample_model_01_db

def sample_model_02_views_function(request):
    if request.method == 'POST':
        sample_model_02_db = SampleModel02_Forms(request.POST)
        if sample_model_02_db.is_valid():
            sample_model_02_db.save(commit=True)
            print(sample_model_02_db.cleaned_data)
    else:
        sample_model_02_db = SampleModel02_Forms()
    return sample_model_02_db

def sample_model_03_views_function(request):
    if request.method == 'POST':
        sample_model_03_db = SampleModel03_Forms(request.POST)
        if sample_model_03_db.is_valid():
            sample_model_03_db.save(commit=True)
            print(sample_model_03_db.cleaned_data)
    else:
        sample_model_03_db = SampleModel03_Forms()
    return sample_model_03_db
