# Generated by Django 5.0.7 on 2024-07-22 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textileapp', '0004_alter_products_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]