# Generated by Django 5.0.4 on 2024-05-15 17:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0003_alter_carpart_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="carpart",
            name="order",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="car_parts",
                to="store.order",
            ),
        ),
    ]