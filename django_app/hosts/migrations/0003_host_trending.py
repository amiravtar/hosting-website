# Generated by Django 4.1.3 on 2022-12-03 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hosts", "0002_host_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="host",
            name="trending",
            field=models.BooleanField(default=False, verbose_name="Trending"),
        ),
    ]
