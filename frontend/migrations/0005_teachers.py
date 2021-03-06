# Generated by Django 2.2.7 on 2020-03-22 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_auto_20200321_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('subject', models.TextField()),
                ('qualification', models.TextField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='pics')),
                ('facebook', models.URLField()),
                ('google', models.URLField()),
                ('linkedin', models.URLField()),
            ],
        ),
    ]
