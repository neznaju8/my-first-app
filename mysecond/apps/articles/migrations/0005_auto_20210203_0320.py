# Generated by Django 3.1.2 on 2021-02-03 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20210203_0318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='answer_date',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='answer_image',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='comment_date',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='comment_image',
        ),
    ]
