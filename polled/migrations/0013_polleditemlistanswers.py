# Generated by Django 2.2.5 on 2019-09-22 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smena_tests', '0015_auto_20190920_1520'),
        ('polled', '0012_auto_20190922_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='PolledItemListAnswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_right', models.BooleanField(default=False)),
                ('is_selected', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('polled_answer', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='smena_tests.Answer')),
            ],
            options={
                'verbose_name': 'Polled Item List',
                'verbose_name_plural': 'Polled Item Lists',
            },
        ),
    ]
