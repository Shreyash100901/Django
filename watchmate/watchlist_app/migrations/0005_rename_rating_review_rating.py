# Generated by Django 5.1.3 on 2024-11-08 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0004_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='Rating',
            new_name='rating',
        ),
    ]
