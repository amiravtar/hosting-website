# Generated by Django 4.1.3 on 2022-12-03 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("hosts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="host",
            name="category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="hosts.hostcategory",
                verbose_name="Category",
            ),
            preserve_default=False,
        ),
    ]