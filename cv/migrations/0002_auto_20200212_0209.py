# Generated by Django 2.0.4 on 2020-02-11 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicinformation',
            name='info',
            field=models.TextField(),
        ),
    ]
