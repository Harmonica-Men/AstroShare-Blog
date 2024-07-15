# Generated by Django 4.2.13 on 2024-07-15 05:38

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogger', '0006_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True)),
                ('profile_pic', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('website_url', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter_url', models.CharField(blank=True, max_length=100, null=True)),
                ('instagram_url', models.CharField(blank=True, max_length=100, null=True)),
                ('facebook_url', models.CharField(blank=True, max_length=100, null=True)),
                ('pinterest', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
