# Generated by Django 4.2.6 on 2023-10-23 22:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("userprofiles", "0002_alter_profile_stars"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="profile_picture",
            field=models.ImageField(blank=True, null=True, upload_to="userprofiles"),
        ),
    ]
