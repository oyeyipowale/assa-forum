# Generated by Django 2.1.7 on 2019-03-06 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='url',
        ),
    ]
