# Generated by Django 2.2.11 on 2020-04-26 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewelry', '0006_auto_20200425_2208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='production',
            old_name='image',
            new_name='background',
        ),
        migrations.AddField(
            model_name='production',
            name='image1',
            field=models.ImageField(default='null', upload_to='production/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='production',
            name='image2',
            field=models.ImageField(default='null', upload_to='production/%Y/%m/%d'),
        ),
    ]
