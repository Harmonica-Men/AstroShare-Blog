# Generated by Django 4.2.13 on 2024-07-11 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='{{ post.title }}', max_length=200),
        ),
    ]
