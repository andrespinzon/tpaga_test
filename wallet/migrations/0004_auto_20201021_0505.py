# Generated by Django 3.1.2 on 2020-10-21 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0003_auto_20201021_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='description',
            field=models.CharField(max_length=255, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='order',
            name='tpaga_transaction',
            field=models.JSONField(default=dict, verbose_name='Tpaga Transaction'),
        ),
    ]
