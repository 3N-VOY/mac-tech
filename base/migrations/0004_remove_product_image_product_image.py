# Generated by Django 4.2.6 on 2023-10-25 17:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0003_alter_picture_picture_alter_product_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="image",
        ),
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ManyToManyField(blank=True, null=True, to="base.picture"),
        ),
    ]
