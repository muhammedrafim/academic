# Generated by Django 2.2.7 on 2020-03-25 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0014_gallery_maingalleryimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='displayimage',
            field=models.ImageField(default='this', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
