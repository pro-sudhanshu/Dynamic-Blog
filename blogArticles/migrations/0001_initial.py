# Generated by Django 4.2.15 on 2024-09-07 15:01

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=255)),
                ('post_content', models.TextField()),
                ('post_category', models.CharField(choices=[('Technology', 'Technology'), ('Education', 'Education')], max_length=100)),
                ('post_published_date', models.DateTimeField(auto_now_add=True)),
                ('post_slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='post_title', unique=True)),
            ],
        ),
    ]
