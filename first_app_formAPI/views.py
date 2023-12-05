from django.shortcuts import render
from .forms import (SampleForm01, SampleForm02, SampleForm03, SampleForm04,
                    SampleForm05, SampleForm06, SampleForm07, SampleForm08,
                    SampleForm09, SampleForm10, SampleForm11, SampleForm12)

# Create your views here.
def home(request):
    return render(request, 'first_app_formAPI/home.html')

def ordinarycoders(request):
    form01 = sample_form_01_views_function(request)
    form02 = sample_form_02_views_function(request)
    form03 = sample_form_03_views_function(request)
    form04 = sample_form_04_views_function(request)
    form05 = sample_form_05_views_function(request)
    form06 = sample_form_06_views_function(request)
    form07 = sample_form_07_views_function(request)
    form08 = sample_form_08_views_function(request)
    form09 = sample_form_09_views_function(request)
    form10 = sample_form_10_views_function(request)
    form11 = sample_form_11_views_function(request)
    form12 = sample_form_12_views_function(request)

    context = {
        'form01': form01,
        'form02': form02,
        'form03': form03,
        'form04': form04,
        'form05': form05,
        'form06': form06,
        'form07': form07,
        'form08': form08,
        'form09': form09,
        'form10': form10,
        'form11': form11,
        'form12': form12,
    }

    return render(request, 'first_app_formAPI/ordinarycoders.html', context)

def sample_form_01_views_function(request):
    if request.method == 'POST':
        form = SampleForm01(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = SampleForm01()
    return form

def sample_form_02_views_function(request):
    if request.method == 'POST':
        form = SampleForm02(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = SampleForm02()
    return form

def sample_form_03_views_function(request):
    if request.method == 'POST':
        form = SampleForm03(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = SampleForm03()
    return form

def sample_form_04_views_function(request):
    if request.method == 'POST':
        form = SampleForm04(request.POST)
        if form.is_valid():
            pass
            # print(form.cleaned_data)
    else:
        form = SampleForm04()
    return form

def sample_form_05_views_function(request):
    if request.method == 'POST':
        form = SampleForm05(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = SampleForm05()
    return form

def sample_form_06_views_function(request):
    if request.method == 'POST':
        form = SampleForm06(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = SampleForm06()
    return form

def sample_form_07_views_function(request):
    if request.method == 'POST':
        form = SampleForm07(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = SampleForm07()
    return form

def sample_form_08_views_function(request):
    if request.method == 'POST':
        form = SampleForm08(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = SampleForm08()
    return form

def sample_form_09_views_function(request):
    if request.method == 'POST':
        form = SampleForm09(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = SampleForm09()
    return form

def sample_form_10_views_function(request):
    if request.method == 'POST':
        form = SampleForm10(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = SampleForm10()
    return form

def sample_form_11_views_function(request):
    if request.method == 'POST':
        form = SampleForm11(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = SampleForm11()
    return form

def sample_form_12_views_function(request):
    if request.method == 'POST':
        form = SampleForm12(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = SampleForm12()
    return form
