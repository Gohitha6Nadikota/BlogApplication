# Generated by Django 5.1.4 on 2025-01-09 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApplication', '0002_post_titl_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='titl_tag',
            new_name='title_tag',
        ),
    ]
