# Generated by Django 4.2.5 on 2023-10-08 11:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profile_photo",
            field=models.ImageField(
                upload_to="images/default_photo.jpeg", verbose_name="Profile photo"
            ),
        ),
    ]
