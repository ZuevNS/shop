# Generated by Django 2.1.7 on 2019-03-21 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_subscriber_usr_bday'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='sex',
            field=models.CharField(choices=[('Ж', 'Женский'), ('М', 'Мужской')], default='М', max_length=1),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='usr_bday',
            field=models.DateField(),
        ),
    ]
