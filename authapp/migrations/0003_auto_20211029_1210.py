# Generated by Django 3.2 on 2021-10-29 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20211026_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='linked_worker',
        ),
        migrations.AddField(
            model_name='customuser',
            name='phones',
            field=models.TextField(blank=True, verbose_name='Телефоны'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='telegram_id',
            field=models.IntegerField(default=0, verbose_name='Telegram ID'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email'),
        ),
    ]
