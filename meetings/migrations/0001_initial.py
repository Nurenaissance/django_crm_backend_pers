# Generated by Django 2.0.5 on 2018-05-04 22:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='meetings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, blank=True, null=True, verbose_name='Title')),
                ('location', models.CharField(max_length=255, blank=True, null=True, verbose_name='Location')),
                ('from', models.DateTimeField(verbose_name='From',null=True, blank=True)),
                ('to', models.DateTimeField(verbose_name='To',null=True, blank=True)),
                ('related_to', models.CharField(max_length=255, blank=True, null=True, verbose_name='Related To')),
                ('contact_name', models.CharField(max_length=255, blank=True, null=True, verbose_name='Contact Name')),
                ('host', models.CharField(max_length=255, blank=True, null=True, verbose_name='Host')),
                ('participants', models.CharField(max_length=255, blank=True, null=True, verbose_name='Participants')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=models.CASCADE, related_name='meetings', to='accounts.Account')),
                ('assigned_to', models.ManyToManyField(related_name='meeting_assigned_users', to=settings.AUTH_USER_MODEL)),
                ('createdBy', models.ForeignKey(on_delete=models.CASCADE, related_name='meeting_created_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]