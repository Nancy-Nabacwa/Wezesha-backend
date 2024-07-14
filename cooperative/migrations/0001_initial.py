# Generated by Django 5.0.7 on 2024-07-14 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cooperative",
            fields=[
                ("id", models.SmallIntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=255, unique=True)),
                ("phone_number", models.CharField(max_length=20)),
            ],
        ),
    ]
