# Generated by Django 2.2.5 on 2019-09-20 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polled', '0003_auto_20190920_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='polleditemlist',
            name='polled',
            field=models.ForeignKey(blank=True, default=None, max_length=128, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='polled.Polled'),
        ),
    ]
