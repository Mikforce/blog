# Generated by Django 4.0.3 on 2022-04-08 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Коментарий', 'verbose_name_plural': 'Коментарии'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(max_length=200, verbose_name='текст коментария'),
        ),
    ]
