# Generated by Django 4.2.7 on 2023-11-08 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('branchId', models.IntegerField(primary_key=True)),
                ('address', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productId', models.IntegerField(primary_key=True)),
                ('price', models.FloatField()),
                ('category', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
            ],
        ),
    ]
