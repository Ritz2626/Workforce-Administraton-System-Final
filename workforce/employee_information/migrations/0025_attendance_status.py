# Generated by Django 4.0.6 on 2023-05-12 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0024_alter_attendance_employee_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='status',
            field=models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Excused', 'Excused')], default='Absent', max_length=20),
        ),
    ]
