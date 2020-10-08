# Generated by Django 3.0.5 on 2020-10-08 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="address",
            field=models.CharField(
                db_index=True, max_length=512, verbose_name="Address"
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="email",
            field=models.EmailField(db_index=True, max_length=64, verbose_name="Email"),
        ),
    ]
