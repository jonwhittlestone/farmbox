# Generated by Django 3.0.5 on 2020-06-26 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20200625_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]