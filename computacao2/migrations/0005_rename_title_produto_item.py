# Generated by Django 3.2.8 on 2022-05-16 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computacao2', '0004_auto_20220515_2117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='title',
            new_name='item',
        ),
    ]
