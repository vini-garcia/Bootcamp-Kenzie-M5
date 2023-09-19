# Generated by Django 4.2.4 on 2023-08-21 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0002_initial"),
        ("contents", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="content",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="contents",
                to="courses.course",
            ),
        ),
    ]