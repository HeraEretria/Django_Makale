# Generated by Django 4.2.4 on 2023-09-07 16:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("article", "0004_alter_article_content_comment"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="article",
            options={"ordering": ["-created_date"]},
        ),
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ["-comment_date"]},
        ),
        migrations.AlterField(
            model_name="comment",
            name="comment_content",
            field=models.TextField(verbose_name="Yorum"),
        ),
    ]
