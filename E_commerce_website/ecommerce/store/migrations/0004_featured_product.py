# Generated by Django 4.2.3 on 2023-09-02 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_customer_phone_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='featured_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]