# Generated by Django 3.0.3 on 2020-04-10 07:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator('адрес должен быть корректным')], verbose_name='адрес почты')),
                ('name', models.CharField(max_length=128, verbose_name='имя')),
            ],
            options={
                'verbose_name': 'подписчик',
                'verbose_name_plural': 'подписчики',
                'ordering': ['name'],
            },
        ),
    ]