# Generated by Django 3.0.2 on 2020-02-09 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0002_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='Email',
            field=models.CharField(default='null', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='position',
            field=models.CharField(default='null', max_length=20),
            preserve_default=False,
        ),
    ]