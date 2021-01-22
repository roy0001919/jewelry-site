# Generated by Django 3.0.4 on 2020-03-28 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField(default='null', max_length=1000)),
                ('image', models.ImageField(default='null', upload_to='production/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null', max_length=250)),
                ('image', models.ImageField(default='null', upload_to='collection/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='null', upload_to='production/%Y/%m/%d')),
                ('serviceEmail', models.CharField(default='null', max_length=250)),
                ('servicePhone', models.CharField(default='null', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=1, max_length=250)),
                ('price', models.CharField(blank=True, default=1, max_length=250)),
                ('discount', models.CharField(blank=True, default=1, max_length=250)),
                ('image', models.ImageField(blank=True, default=1, upload_to='production/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Jewelry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null', max_length=250)),
                ('length', models.CharField(default='null', max_length=250)),
                ('width', models.CharField(default='null', max_length=250)),
                ('thickness', models.CharField(default='null', max_length=250)),
                ('weight', models.CharField(default='null', max_length=250)),
                ('category', models.CharField(default='null', max_length=250)),
                ('image', models.ImageField(default='null', upload_to='upload/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='null', max_length=250)),
                ('content', models.TextField(default='null', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null', max_length=250)),
                ('content', models.CharField(default='null', max_length=250)),
                ('idea', models.TextField(default='null', max_length=1000)),
                ('image', models.ImageField(default='null', upload_to='production/%Y/%m/%d')),
                ('remark', models.TextField(default='null', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='QA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='null', max_length=250)),
                ('content', models.TextField(default='null', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Sketch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='null', upload_to='production/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='MyAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tshirts_ids', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Tshirts_goods', to='jewelry.Goods')),
                ('clothes_ids', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='clothes_goods', to='jewelry.Goods')),
                ('hoodies_ids', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='hoodies_goods', to='jewelry.Goods')),
                ('music_ids', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='music_goods', to='jewelry.Goods')),
                ('posters_ids', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posters_goods', to='jewelry.Goods')),
                ('uncategorized_ids', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='uncategorized_goods', to='jewelry.Goods')),
            ],
        ),
    ]