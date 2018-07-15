# Generated by Django 2.0.5 on 2018-07-14 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bowling', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='frame',
            name='isFinished',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='frame',
            name='throwIndex',
            field=models.IntegerField(choices=[(0, 0), (1, 1)], default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='currentFrameIndex',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='currentThrowIndex',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='gameOver',
            field=models.BooleanField(default=False),
        ),
    ]