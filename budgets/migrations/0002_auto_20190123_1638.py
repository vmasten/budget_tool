# Generated by Django 2.1.5 on 2019-01-23 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='remaining_budget',
            field=models.FloatField(),
        ),
    ]
