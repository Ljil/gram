# Generated by Django 3.0.6 on 2020-05-16 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20200514_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(related_name='movies', to='movies.Genre', verbose_name='Жанры'),
        ),
    ]
