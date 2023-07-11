# Generated by Django 4.2 on 2023-06-21 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btb1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rd',
            name='desc',
            field=models.CharField(default='Default description', max_length=255),
        ),
        migrations.AddField(
            model_name='rd',
            name='space',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
