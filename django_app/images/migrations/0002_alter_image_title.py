# Generated by Django 4.1.3 on 2022-12-03 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("images", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="title",
            field=models.CharField(max_length=20, unique=True, verbose_name="Title"),
        ),
    ]
