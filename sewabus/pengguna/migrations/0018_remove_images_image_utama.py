# Generated by Django 2.2 on 2020-12-18 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pengguna', '0017_auto_20201218_0012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='image_utama',
        ),
    ]
