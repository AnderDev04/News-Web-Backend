# Generated by Django 5.0.6 on 2024-08-21 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_category_news_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
