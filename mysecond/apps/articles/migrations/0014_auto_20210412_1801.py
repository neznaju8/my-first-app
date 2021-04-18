# Generated by Django 3.1.2 on 2021-04-12 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_auto_20210412_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.SlugField(default='', max_length=160, unique=True, verbose_name='slug'),
        ),
    ]