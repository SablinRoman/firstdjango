# Generated by Django 3.0.2 on 2020-03-25 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0006_auto_20200323_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='room',
            field=models.FloatField(blank=True, db_index=True),
        ),
    ]
