# Generated by Django 2.2.5 on 2019-12-05 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smena_tests', '0022_auto_20191022_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='name_poll',
            field=models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Имя теста'),
        ),
    ]
