# Generated by Django 5.1.3 on 2024-12-05 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_alter_postsresponses_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postsresponses',
            name='text',
            field=models.CharField(max_length=400, verbose_name='Текст'),
        ),
    ]