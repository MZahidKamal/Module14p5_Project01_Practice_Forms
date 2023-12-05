from django.urls import path
from .views import home, ordinarycoders

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('ordinarycoders/', ordinarycoders, name='ordinarycoders'),
]
