# Generated by Django 3.2 on 2023-02-07 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_dados_semanal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semanal',
            name='estoque',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='semanal',
            name='projecao_m0',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='semanal',
            name='real',
            field=models.FloatField(null=True),
        ),
    ]
