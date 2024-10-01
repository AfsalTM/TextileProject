# Generated by Django 5.0.7 on 2024-07-22 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textileapp', '0002_alter_category_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=50, null=True)),
                ('product_name', models.CharField(blank=True, max_length=50, null=True)),
                ('brand', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.IntegerField(blank=True, max_length=50, null=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='product_image')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='product_image')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='product_image')),
            ],
        ),
    ]