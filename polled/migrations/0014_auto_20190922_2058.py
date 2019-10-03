# Generated by Django 2.2.5 on 2019-09-22 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polled', '0013_polleditemlistanswers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='polleditemlistanswers',
            options={'verbose_name': 'Polled Item List Answers', 'verbose_name_plural': 'Polled Item List Answers'},
        ),
        migrations.AddField(
            model_name='polleditemlistanswers',
            name='polled',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='polled.PolledItemList'),
        ),
    ]
