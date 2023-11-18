# Generated by Django 4.2.7 on 2023-11-11 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("Clients", "0001_initial"),
    ]

    operations = [

        migrations.AddField(
            model_name="corporation",
            name="clientinfo_ptr",
            field=models.OneToOneField(
                auto_created=True,
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                to="Clients.clientinfo",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="person",
            name="clientinfo_ptr",
            field=models.OneToOneField(
                auto_created=True,
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                to="Clients.clientinfo",
            ),
            preserve_default=False,
        ),
    ]