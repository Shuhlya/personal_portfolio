# Generated by Django 3.2.18 on 2023-05-12 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_description_blog_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
