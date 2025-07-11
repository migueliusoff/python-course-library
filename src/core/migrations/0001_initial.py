# Generated by Django 5.2.1 on 2025-05-15 08:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Library",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "библиотека",
                "verbose_name_plural": "библиотеки",
            },
        ),
        migrations.CreateModel(
            name="Hall",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "library",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="halls",
                        to="core.library",
                        verbose_name="библиотека",
                    ),
                ),
            ],
            options={
                "verbose_name": "зал",
                "verbose_name_plural": "залы",
            },
        ),
        migrations.CreateModel(
            name="Rack",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "hall",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="racks",
                        to="core.hall",
                        verbose_name="зал",
                    ),
                ),
            ],
            options={
                "verbose_name": "стеллаж",
                "verbose_name_plural": "стеллажи",
            },
        ),
        migrations.CreateModel(
            name="Shelf",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "rack",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="shelves",
                        to="core.rack",
                        verbose_name="стеллаж",
                    ),
                ),
            ],
            options={
                "verbose_name": "полка",
                "verbose_name_plural": "полки",
            },
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(verbose_name="название")),
                ("authors", models.TextField(verbose_name="авторы")),
                ("published_on_year", models.PositiveSmallIntegerField(verbose_name="год издания")),
                (
                    "shelf",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="books",
                        to="core.shelf",
                        verbose_name="полка",
                    ),
                ),
            ],
            options={
                "verbose_name": "книга",
                "verbose_name_plural": "книги",
            },
        ),
    ]
