# Generated by Django 3.0.6 on 2020-05-14 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='death_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата смерти'),
        ),
    ]
