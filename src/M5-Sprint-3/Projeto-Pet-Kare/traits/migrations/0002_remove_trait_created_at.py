# Generated by Django 4.2.3 on 2023-08-02 17:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("traits", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="trait",
            name="created_at",
        ),
    ]
