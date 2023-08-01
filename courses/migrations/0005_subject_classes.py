# Generated by Django 4.2.3 on 2023-08-01 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_remove_course_discount_course_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('professor', models.CharField(max_length=200)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('schedule', models.JSONField(verbose_name={'end_date': models.CharField(max_length=200), 'start_date': models.CharField(max_length=200)})),
                ('hasTest', models.BooleanField(default=False)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='courses.subject')),
            ],
        ),
    ]