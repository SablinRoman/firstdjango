# Generated by Django 3.0.2 on 2020-02-10 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0002_auto_20200210_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='place_status',
            field=models.CharField(db_index=True, default='пусто', max_length=25),
        ),
    ]
