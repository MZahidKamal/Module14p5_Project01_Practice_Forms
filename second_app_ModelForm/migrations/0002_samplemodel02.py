# Generated by Django 5.0 on 2023-12-05 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_app_ModelForm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SampleModel02',
            fields=[
                ('auto_field', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
