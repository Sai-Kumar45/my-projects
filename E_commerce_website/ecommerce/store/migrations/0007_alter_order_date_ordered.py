# Generated by Django 4.2.4 on 2023-09-03 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_shippingaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]