# Generated by Django 5.1.4 on 2025-01-15 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApplication', '0007_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click the above link to read the post', max_length=255),
        ),
    ]