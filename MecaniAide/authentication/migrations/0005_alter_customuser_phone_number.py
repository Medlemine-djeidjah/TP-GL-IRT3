# Generated by Django 5.0.4 on 2024-05-25 23:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0004_alter_customuser_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="phone_number",
            field=models.CharField(max_length=15, unique=True),
        ),
    ]