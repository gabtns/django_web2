# Generated by Django 4.2.5 on 2023-09-22 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("servicio", "0003_alter_servicios_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="servicios", old_name="image", new_name="images",
        ),
    ]