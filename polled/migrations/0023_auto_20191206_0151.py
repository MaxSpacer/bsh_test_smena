# Generated by Django 2.2.5 on 2019-12-05 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polled', '0022_auto_20191022_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polled',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата начала теста'),
        ),
        migrations.AlterField(
            model_name='polled',
            name='is_done',
            field=models.BooleanField(default=False, verbose_name='завершен?'),
        ),
        migrations.AlterField(
            model_name='polled',
            name='polled_poll',
            field=models.ForeignKey(blank=True, default=None, max_length=128, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='smena_tests.Poll', verbose_name='тест'),
        ),
        migrations.AlterField(
            model_name='polleditemlistanswers',
            name='is_right',
            field=models.BooleanField(default=False, verbose_name='верен/неверен'),
        ),
        migrations.AlterField(
            model_name='polleditemlistanswers',
            name='is_selected',
            field=models.BooleanField(default=False, verbose_name='выбор тестируемого'),
        ),
    ]
