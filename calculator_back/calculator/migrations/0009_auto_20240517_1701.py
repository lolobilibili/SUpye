# Generated by Django 3.0 on 2024-05-17 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0008_auto_20240517_1700'),
    ]

    operations = [
        migrations.DeleteModel(
            name='breakfast',
        ),
        migrations.DeleteModel(
            name='dinner',
        ),
        migrations.DeleteModel(
            name='lunch',
        ),
        migrations.DeleteModel(
            name='snack',
        ),
        migrations.DeleteModel(
            name='sport',
        ),
    ]