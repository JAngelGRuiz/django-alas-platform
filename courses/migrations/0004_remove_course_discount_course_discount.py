# Generated by Django 4.2.3 on 2023-08-01 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_rename_discounts_course_discount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='discount',
        ),
        migrations.AddField(
            model_name='course',
            name='discount',
            field=models.ManyToManyField(to='courses.discount'),
        ),
    ]
