# Generated by Django 2.2.7 on 2020-04-03 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentdashboard', '0010_marks'),
    ]

    operations = [
        migrations.AddField(
            model_name='marks',
            name='remarks',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
