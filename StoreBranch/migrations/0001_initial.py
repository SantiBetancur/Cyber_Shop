# Generated by Django 4.2.7 on 2023-11-08 04:47

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branchId', models.IntegerField()),
                ('dirección', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productId', models.IntegerField()),
                ('price', models.FloatField()),
                ('category', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('productBranchId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StoreBranch.branch')),
            ],
        ),
    ]