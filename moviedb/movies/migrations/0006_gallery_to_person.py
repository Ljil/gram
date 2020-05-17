# Generated by Django 3.0.6 on 2020-05-17 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20200517_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='to_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='movies.Person'),
        ),
    ]
