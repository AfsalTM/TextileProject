# Generated by Django 5.0.7 on 2024-08-26 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textileapp', '0005_products_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='orderdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
