# Generated by Django 4.2.3 on 2023-08-01 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Discounts',
            new_name='Discount',
        ),
        migrations.RenameModel(
            old_name='Types',
            new_name='Type',
        ),
    ]
