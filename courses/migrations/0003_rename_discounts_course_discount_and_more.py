# Generated by Django 4.2.3 on 2023-08-01 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_rename_discounts_discount_rename_types_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='discounts',
            new_name='discount',
        ),
        migrations.AddField(
            model_name='discount',
            name='discount_percentage',
            field=models.IntegerField(default=0.0),
        ),
        migrations.AddField(
            model_name='discount',
            name='type',
            field=models.CharField(default=0.0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='type',
            name='value',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]