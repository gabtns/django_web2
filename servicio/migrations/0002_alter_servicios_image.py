# Generated by Django 4.2.5 on 2023-09-21 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("servicio", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="servicios",
            name="image",
            field=models.ImageField(upload_to="servi", verbose_name="imagen"),
        ),
    ]
