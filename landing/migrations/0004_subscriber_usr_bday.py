# Generated by Django 2.1.7 on 2019-03-21 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_auto_20190319_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='usr_bday',
            field=models.DateField(auto_now=True),
        ),
    ]