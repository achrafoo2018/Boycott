# Generated by Django 2.2 on 2019-05-02 17:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=500, validators=[django.core.validators.RegexValidator(code='nomatch', message='Text should contain at least 20 Charcters', regex='.{20,}')]),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(code='nomatch', message='Title should contain at least 5 Charcters', regex='.{5,}')]),
        ),
    ]
