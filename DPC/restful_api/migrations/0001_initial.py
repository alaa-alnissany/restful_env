# Generated by Django 5.0.4 on 2024-05-17 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Device",
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
                ("battery_power", models.PositiveIntegerField()),
                ("clock_speed", models.FloatField()),
                ("int_memory", models.FloatField()),
                ("m_dep", models.FloatField()),
                ("mobile_wt", models.FloatField()),
                ("n_cores", models.PositiveIntegerField()),
                ("fc", models.FloatField()),
                ("pc", models.FloatField()),
                ("px_height", models.PositiveIntegerField()),
                ("px_width", models.PositiveIntegerField()),
                ("ram", models.PositiveIntegerField()),
                ("sc_h", models.FloatField()),
                ("sc_w", models.FloatField()),
                ("talk_time", models.FloatField()),
                ("four_g", models.BooleanField(default=False)),
                ("tree_g", models.BooleanField(default=False)),
                ("touch_screen", models.BooleanField(default=False)),
                ("dual_sim", models.BooleanField(default=False)),
                ("wifi", models.BooleanField(default=False)),
                ("blue", models.BooleanField(default=False)),
                ("price_range", models.IntegerField(default=-1)),
            ],
        ),
    ]
