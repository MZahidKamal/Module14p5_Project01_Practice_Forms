from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'first_app_formAPI/home.html')

def about(request):
    return render(request, 'first_app_formAPI/about.html')
