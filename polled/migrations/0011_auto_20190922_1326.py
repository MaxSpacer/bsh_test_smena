# Generated by Django 2.2.5 on 2019-09-22 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polled', '0010_auto_20190922_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polled',
            name='finish_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
