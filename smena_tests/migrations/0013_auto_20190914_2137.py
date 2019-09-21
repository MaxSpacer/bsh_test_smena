# Generated by Django 2.2.5 on 2019-09-14 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smena_tests', '0012_auto_20190914_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollitemlist',
            name='quest_category_type',
            field=models.ForeignKey(choices=[('1', 'Сетевая архитектура'), ('2', 'Взаимодействие с клиентами'), ('3', 'Диагностика проблем'), ('4', 'Диагностика проблем c HS')], default='Сетевая архитектура', max_length=256, on_delete=django.db.models.deletion.SET_DEFAULT, to='smena_tests.QuestCategory', verbose_name='категории вопросов'),
        ),
    ]
