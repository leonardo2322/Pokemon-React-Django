# Generated by Django 4.0.6 on 2022-09-24 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_pokemonsbbdd_habilidades'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonsbbdd',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]