# Generated by Django 4.2.6 on 2024-05-21 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "calculator",
            "0013_score_record_remove_user_id_remove_user_group_id_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="score_record",
            name="score",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="score_record",
            name="suggestion",
            field=models.CharField(default="", max_length=200),
        ),
    ]
