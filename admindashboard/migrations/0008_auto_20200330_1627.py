# Generated by Django 2.2.7 on 2020-03-30 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admindashboard', '0007_auto_20200330_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subject_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='admindashboard.Class'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='teacherdashboard.teachers'),
        ),
    ]
