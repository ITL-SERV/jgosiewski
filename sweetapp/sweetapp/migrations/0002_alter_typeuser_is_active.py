# Generated by Django 4.2.5 on 2023-12-11 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sweetapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typeuser',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Aktywny?'),
        ),
    ]
