# Generated by Django 4.2 on 2023-06-22 18:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('btb1', '0010_remove_rd_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user1',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Rd',
        ),
    ]
