# Generated by Django 5.1.3 on 2024-12-03 12:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='video',
            new_name='product_video',
        ),
        migrations.AlterField(
            model_name='productphoto',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='shop.product'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='stars',
            field=models.ImageField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], upload_to=''),
        ),
    ]