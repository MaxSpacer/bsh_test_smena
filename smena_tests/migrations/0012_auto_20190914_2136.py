# Generated by Django 2.2.5 on 2019-09-14 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smena_tests', '0011_auto_20190914_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollitemlist',
            name='quest_category_type',
            field=models.ForeignKey(choices=[('Сетевая архитектура', 1), ('Взаимодействие с клиентами', 2), ('Диагностика проблем', 3), ('Диагностика проблем c HS', 4)], default='Сетевая архитектура', max_length=256, on_delete=django.db.models.deletion.SET_DEFAULT, to='smena_tests.QuestCategory', verbose_name='категории вопросов'),
        ),
    ]
