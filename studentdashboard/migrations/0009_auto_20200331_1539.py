# Generated by Django 2.2.7 on 2020-03-31 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentdashboard', '0008_remove_attendance_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='attendence_blocked',
            field=models.TextField(default='No'),
        ),
    ]
