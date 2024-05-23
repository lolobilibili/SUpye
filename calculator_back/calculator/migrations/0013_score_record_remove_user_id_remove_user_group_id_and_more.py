# Generated by Django 4.2.6 on 2024-05-22 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("calculator", "0012_auto_20240517_1733"),
    ]

    operations = [
        migrations.CreateModel(
            name="Score_record",
            fields=[
                (
                    "username",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("bmi", models.FloatField(default=0)),
                ("vital_capacity", models.IntegerField(default=0)),
                ("run_50", models.FloatField(default=0)),
                ("sit_and_reach", models.FloatField(default=0)),
                ("jump", models.FloatField(default=0)),
                ("Pull_ups_and_sit_ups", models.IntegerField(default=0)),
                ("run_1000", models.FloatField(default=0)),
                ("run_1000_performance", models.CharField(default="", max_length=100)),
                ("bmi_score", models.IntegerField(default=0)),
                ("vital_capacity_score", models.IntegerField(default=0)),
                ("run_50_score", models.IntegerField(default=0)),
                ("sit_and_reach_score", models.IntegerField(default=0)),
                ("jump_score", models.IntegerField(default=0)),
                ("Pull_ups_and_sit_ups_score", models.IntegerField(default=0)),
                ("run_1000_score", models.IntegerField(default=0)),
                ("score", models.FloatField(default=0)),
                ("suggestion", models.CharField(default="", max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name="user",
            name="id",
        ),
        migrations.RemoveField(
            model_name="user_group",
            name="id",
        ),
        migrations.AlterField(
            model_name="breakfast",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="dinner",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="lunch",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="snack",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="sport",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="user_group",
            name="username",
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
