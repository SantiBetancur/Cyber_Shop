# Generated by Django 4.2.7 on 2023-11-14 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0003_remove_clientinfo_idclient_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='corporation',
            name='idClient',
        ),
        migrations.RemoveField(
            model_name='person',
            name='idClient',
        ),
    ]