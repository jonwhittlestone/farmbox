# Generated by Django 3.0.5 on 2020-05-18 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0003_auto_20200428_0520'),
    ]

    operations = [
        migrations.CreateModel(
            name='FulfillmentEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_number', models.CharField(help_text='An event-unique number assigned at order creation to aid in Fulfillment sequencing', max_length=64, null=True, verbose_name='F-Number')),
                ('customer_first_name', models.CharField(max_length=512, verbose_name='First Name')),
                ('customer_last_name', models.CharField(max_length=512, verbose_name='Last Name')),
                ('customer_address', models.CharField(max_length=512, verbose_name='Address')),
                ('customer_postcode', models.CharField(max_length=8, verbose_name='Postcode')),
                ('customer_email', models.EmailField(max_length=64, verbose_name='Email')),
                ('customer_phone', models.CharField(max_length=64, verbose_name='Phone')),
                ('fulfillment_method', models.CharField(choices=[('Delivery', 'Delivery'), ('Collect from Ockley Shop', 'Collection Ockley'), ('Collect from Denbies Shop', 'Collection Denbies')], max_length=30, verbose_name='Delivery / Collect from Ockley Shop /  Collect from Denbies Shop')),
                ('collection_location', models.CharField(blank='N/A', choices=[('Denbies', 'Denbies'), ('Ockley', 'Ockley')], max_length=16, verbose_name='If collection, which shop?')),
                ('notes', models.TextField(blank=True, verbose_name='NOTES')),
                ('archived', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField()),
                ('modified_at', models.DateTimeField()),
                ('fulfillment_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.FulfillmentEvent')),
            ],
            options={
                'ordering': ['f_number'],
            },
        ),
        migrations.CreateModel(
            name='OrderForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=512)),
                ('created_at', models.DateTimeField()),
                ('fulfillment_event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.FulfillmentEvent')),
                ('order', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.Order', verbose_name='Order Succesfully Created?')),
            ],
        ),
        migrations.CreateModel(
            name='ProductQuantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_quantities', to='order.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_quantities', to='product.Product')),
            ],
        ),
        migrations.CreateModel(
            name='OrderFormFailure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.OrderForm', verbose_name='Order Form')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(related_name='products', through='order.ProductQuantity', to='product.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
