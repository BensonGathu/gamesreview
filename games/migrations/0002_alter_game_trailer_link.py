# Generated by Django 3.2.5 on 2021-07-27 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='trailer_link',
            field=models.URLField(max_length=30000),
        ),
    ]
