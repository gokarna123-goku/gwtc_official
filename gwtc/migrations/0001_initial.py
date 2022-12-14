# Generated by Django 4.1.4 on 2022-12-19 02:17

from django.db import migrations, models
import django.db.models.deletion
import gwtc.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("fullname", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.CharField(max_length=255)),
                ("msg_date", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="PortfolioCategory",
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
                ("category_name", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Portfolio",
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
                ("portfolio", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to=gwtc.models.get_file_path)),
                ("published_at", models.DateField(auto_now_add=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gwtc.portfoliocategory",
                    ),
                ),
            ],
        ),
    ]
