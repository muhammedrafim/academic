# Generated by Django 2.2.7 on 2020-03-25 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0012_eventdetail_displayimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventdetail',
            name='details',
            field=models.TextField(default='this is a test detail line fo all of the event that appears there'),
            preserve_default=False,
        ),
    ]
