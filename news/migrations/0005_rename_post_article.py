# Generated by Django 4.2.20 on 2025-05-17 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_comment_body'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Article',
        ),
    ]
