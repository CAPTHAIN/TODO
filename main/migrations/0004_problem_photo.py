# Generated by Django 3.2.9 on 2021-11-17 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_problem_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='photo',
            field=models.ImageField(default=1, upload_to='photos', verbose_name='Фото'),
            preserve_default=False,
        ),
    ]
