# Generated by Django 2.2.7 on 2020-03-29 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admindashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.TextField()),
                ('class_code', models.TextField()),
                ('class_teacher', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]
