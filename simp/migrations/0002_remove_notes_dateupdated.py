# Generated by Django 4.0.4 on 2022-04-15 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='dateUpdated',
        ),
    ]
