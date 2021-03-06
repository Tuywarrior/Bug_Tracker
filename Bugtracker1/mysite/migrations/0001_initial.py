# Generated by Django 4.0.1 on 2022-01-29 20:09

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('OL', 'Organisation-Lead'), ('SDE1', 'SeniorDeveloper'), ('SDE2', 'Developer'), ('SDE2', 'JuniorDeveloper'), ('U', 'User')], max_length=4)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bugs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('description', models.TextField(blank=True)),
                ('severity_level', models.CharField(choices=[('H', 'High'), ('M', 'Medium'), ('L', 'Low')], max_length=4)),
                ('resolved', models.BooleanField(default=False)),
                ('deadline', models.DateTimeField(default=datetime.datetime(2022, 1, 30, 1, 39, 32, 521526))),
                ('visibility', models.IntegerField(default=1)),
                ('resolved_on', models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 30, 1, 39, 32, 526278))),
                ('opened_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('assigned_on', models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 30, 1, 39, 32, 526278))),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignedperson', to=settings.AUTH_USER_MODEL)),
                ('raised_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
