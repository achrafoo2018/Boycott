# Generated by Django 2.2 on 2019-05-29 21:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_rates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=5000, validators=[django.core.validators.RegexValidator(code='nomatch', message='Text should contain at least 30 Charcters', regex='.{30,}')]),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=60, validators=[django.core.validators.RegexValidator(code='nomatch', message='Title should contain at least 5 Charcters', regex='.{5,}')]),
        ),
    ]
