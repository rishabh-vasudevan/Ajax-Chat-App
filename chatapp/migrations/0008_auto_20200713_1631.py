# Generated by Django 3.0.8 on 2020-07-13 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0007_auto_20200713_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
