# Generated by Django 4.2.1 on 2024-04-05 14:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("calls", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="calls",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
