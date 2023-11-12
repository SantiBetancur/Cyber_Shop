# Generated by Django 4.2.7 on 2023-11-12 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StoreBranch', '0002_delete_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('productId', models.IntegerField(primary_key=True, serialize=False)),
                ('price', models.FloatField()),
                ('category', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('productBranchId', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='StoreBranch.branch')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
