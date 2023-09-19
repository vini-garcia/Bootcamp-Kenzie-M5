# Generated by Django 4.2.4 on 2023-08-10 18:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0004_alter_movie_duration_alter_movie_rating_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="duration",
            field=models.CharField(default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="movie",
            name="rating",
            field=models.CharField(
                choices=[
                    ("G", "G"),
                    ("PG", "Pg"),
                    ("PG-13", "Pg 13"),
                    ("R", "R"),
                    ("NC-17", "Nc 17"),
                ],
                default="G",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="movie",
            name="synopsis",
            field=models.TextField(default=None, null=True),
        ),
    ]