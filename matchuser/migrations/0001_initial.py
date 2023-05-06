# Generated by Django 4.1.7 on 2023-04-21 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Matchuser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("create_time", models.CharField(max_length=100)),
                ("matchid", models.IntegerField()),
                ("name", models.CharField(max_length=100)),
                ("reserve1", models.CharField(max_length=100)),
                ("reserve2", models.CharField(max_length=100)),
                ("reserve3", models.CharField(max_length=100)),
                ("reserve4", models.CharField(max_length=100)),
                ("reserve5", models.CharField(max_length=100)),
                ("status", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": "Matchuser",
                "verbose_name_plural": "Matchuser",
                "db_table": "matchuser",
            },
        ),
    ]
