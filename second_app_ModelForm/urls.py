from django.urls import path
from .views import great_devxy_medium

urlpatterns = [
    path('great_devxy_medium/', great_devxy_medium, name='great_devxy_medium'),
]
