# Generated by Django 3.2.20 on 2023-08-17 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0005_alter_trait_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feat',
            old_name='prerequisite_desc',
            new_name='prerequisite',
        ),
    ]