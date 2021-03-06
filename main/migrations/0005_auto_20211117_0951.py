# Generated by Django 3.2.9 on 2021-11-17 07:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_problem_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='author_id',
        ),
        migrations.AddField(
            model_name='problem',
            name='author',
            field=models.CharField(default=1, max_length=255, verbose_name='Автор'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='problem',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Адресат'),
        ),
    ]
