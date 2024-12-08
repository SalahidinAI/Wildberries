# Generated by Django 5.1.3 on 2024-12-03 06:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=32, unique=True)),
                ('category_name_en', models.CharField(max_length=32, null=True, unique=True)),
                ('category_name_ru', models.CharField(max_length=32, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('age', models.PositiveSmallIntegerField()),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('user_image', models.ImageField(blank=True, null=True, upload_to='user_image/')),
                ('status', models.CharField(choices=[('gold', 'gold'), ('silver', 'silver'), ('bronze', 'bronze'), ('simple', 'simple')], default='simple', max_length=16)),
                ('date_register', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=64)),
                ('product_name_en', models.CharField(max_length=64, null=True)),
                ('product_name_ru', models.CharField(max_length=64, null=True)),
                ('description', models.TextField()),
                ('description_en', models.TextField(null=True)),
                ('description_ru', models.TextField(null=True)),
                ('price', models.PositiveIntegerField()),
                ('check_original', models.BooleanField(default=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='product_videos/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.ImageField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], upload_to='')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.userprofile')),
            ],
        ),
    ]