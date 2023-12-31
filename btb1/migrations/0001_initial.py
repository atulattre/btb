# Generated by Django 4.2 on 2023-06-20 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('student_id', models.IntegerField(default=0)),
                ('course', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('year', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Rd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('build_name', models.CharField(max_length=100)),
                ('room_number', models.CharField(max_length=10)),
                ('room_type', models.CharField(max_length=50)),
                ('images', models.ManyToManyField(to='btb1.image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='btb1.user')),
            ],
        ),
    ]
