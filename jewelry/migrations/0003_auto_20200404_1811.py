# Generated by Django 2.2.11 on 2020-04-04 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jewelry', '0002_goods_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goods',
            old_name='discount',
            new_name='originalPrice',
        ),
    ]
