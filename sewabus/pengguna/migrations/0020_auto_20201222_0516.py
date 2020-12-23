# Generated by Django 2.2.12 on 2020-12-22 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pengguna', '0019_images_t_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='t_id',
        ),
        migrations.AlterField(
            model_name='images',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='pengguna.DataBus'),
        ),
    ]
