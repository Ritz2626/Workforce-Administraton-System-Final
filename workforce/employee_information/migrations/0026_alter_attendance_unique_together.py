# Generated by Django 4.0.6 on 2023-05-15 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0025_attendance_status'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together={('employee_id', 'date')},
        ),
    ]
