# Generated by Django 2.2.12 on 2020-12-23 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0016_auto_20201223_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sewa',
            name='no_ktp',
            field=models.CharField(max_length=50, null=True),
        ),
    ]