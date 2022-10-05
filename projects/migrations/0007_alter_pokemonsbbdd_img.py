# Generated by Django 4.0.6 on 2022-10-04 03:21

from django.db import migrations, models
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_pokemonsbbdd_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonsbbdd',
            name='img',
            field=models.ImageField(blank=True, default='images/squirtle.png', null=True, upload_to=projects.models.upload_to, verbose_name='images'),
        ),
    ]
