# Generated by Django 4.0.3 on 2022-03-11 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_mensalista'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensalista',
            name='inicio',
            field=models.DateField(),
        ),
    ]
