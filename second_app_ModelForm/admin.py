from django.contrib import admin
from second_app_ModelForm.models import (SampleModel01, SampleModel02, SampleModel03)

# Register your models here.
# admin.site.register(SampleModel01)

@admin.register(SampleModel01)
class SampleModel01Admin(admin.ModelAdmin):
    list_display = ('name', 'id')

@admin.register(SampleModel02)
class SampleModel02Admin(admin.ModelAdmin):
    list_display = ('auto_field', 'name')

@admin.register(SampleModel03)
class SampleModel03Admin(admin.ModelAdmin):
    list_display = ('big_auto_field', 'name')
