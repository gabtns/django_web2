# Generated by Django 4.2.5 on 2023-09-22 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("servicio", "0005_servicios_precios"),
    ]

    operations = [
        migrations.AlterField(
            model_name="servicios",
            name="images",
            field=models.ImageField(upload_to="servicios", verbose_name="imagen"),
        ),
    ]
