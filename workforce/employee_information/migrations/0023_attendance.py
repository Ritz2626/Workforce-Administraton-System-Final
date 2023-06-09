# Generated by Django 4.0.6 on 2023-05-12 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0022_project_files'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intime', models.TimeField()),
                ('outime', models.TimeField()),
                ('date', models.DateField(blank=True)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_information.project')),
            ],
        ),
    ]
