# Generated by Django 3.1.2 on 2020-10-05 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0005_auto_20201005_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='number',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
