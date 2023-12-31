# Generated by Django 4.2.4 on 2023-08-21 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("students_courses", "0001_initial"),
        ("courses", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="instructor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="courses",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="course",
            name="students",
            field=models.ManyToManyField(
                related_name="my_courses",
                through="students_courses.StudentCourse",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
