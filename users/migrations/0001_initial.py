# Generated by Django 5.1.4 on 2024-12-17 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("address", models.TextField(null=True)),
                ("contact", models.CharField(max_length=50, null=True)),
                (
                    "gender",
                    models.CharField(
                        choices=[("MALE", "Male"), ("FEMALE", "Female")], max_length=6
                    ),
                ),
                ("is_staff", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "User",
                "verbose_name_plural": "Users",
                "db_table": "users",
                "ordering": ["last_name", "first_name"],
            },
        ),
    ]
