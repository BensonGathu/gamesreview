# Generated by Django 3.2.5 on 2021-07-28 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_remove_game_trailer_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='contact',
            field=models.IntegerField(null=True),
        ),
    ]
