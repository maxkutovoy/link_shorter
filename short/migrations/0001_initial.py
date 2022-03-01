# Generated by Django 4.0.2 on 2022-03-01 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_link', models.URLField(verbose_name='Ссылка')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Короткая ссылка')),
            ],
        ),
    ]
