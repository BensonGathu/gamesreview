# Generated by Django 3.2.5 on 2021-07-29 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0016_alter_query_forum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='forum',
        ),
        migrations.AddField(
            model_name='profile',
            name='forum',
            field=models.ManyToManyField(null=True, related_name='user_forum', to='games.Forum'),
        ),
    ]
