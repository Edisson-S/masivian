# Generated by Django 3.1.2 on 2020-10-05 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_bet'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bet',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]