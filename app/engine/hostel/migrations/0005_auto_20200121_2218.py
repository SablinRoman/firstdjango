# Generated by Django 3.0.2 on 2020-01-21 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0004_auto_20200121_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='contract_number',
            field=models.CharField(blank=True, db_index=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='mobile_number',
            field=models.BigIntegerField(blank=True, db_index=True, default=None, null=True),
        ),
    ]
