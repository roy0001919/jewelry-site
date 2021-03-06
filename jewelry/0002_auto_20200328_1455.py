# Generated by Django 3.0.4 on 2020-03-28 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewelry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='discount',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='goods',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='production/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='name',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
    ]
