# Generated by Django 3.2 on 2023-02-07 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Semanal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('cliente', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('projecao_m0', models.FloatField()),
                ('real', models.FloatField()),
                ('estoque', models.FloatField()),
            ],
        ),
    ]