# Generated by Django 5.1.4 on 2025-01-11 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogging", "0002_category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
        migrations.RemoveField(
            model_name="category",
            name="posts",
        ),
        migrations.AddField(
            model_name="post",
            name="categories",
            field=models.ManyToManyField(
                blank=True, related_name="posts", to="blogging.category"
            ),
        ),
    ]
