# Generated by Django 3.2.5 on 2021-07-28 04:30

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_game_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='video',
            field=embed_video.fields.EmbedVideoField(default=1),
            preserve_default=False,
        ),
    ]
