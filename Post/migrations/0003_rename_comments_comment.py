# Generated by Django 4.0 on 2022-01-14 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_comments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]
