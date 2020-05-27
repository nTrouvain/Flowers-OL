# Generated by Django 3.0.5 on 2020-05-13 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface_app', '0007_dynamicprops_nb_sess'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jold_participant',
            name='nb_sess_finished',
        ),
        migrations.RemoveField(
            model_name='jold_participant',
            name='nb_sess_started',
        ),
        migrations.AddField(
            model_name='participantprofile',
            name='nb_sess_finished',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='participantprofile',
            name='nb_sess_started',
            field=models.IntegerField(default=0),
        ),
    ]