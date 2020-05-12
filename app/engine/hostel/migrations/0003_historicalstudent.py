# Generated by Django 3.0.6 on 2020-05-12 07:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hostel', '0002_cardsfilter'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalStudent',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('bed_status', models.CharField(blank=True, choices=[('Студент', 'Студент'), ('Заочник', 'Заочник'), ('Семейник', 'Семейник'), ('Расселитель', 'Расселитель'), ('Староста этажа', 'Староста этажа'), ('Актив этажа', 'Актив этажа'), ('Санитарная комиссия', 'Санитарная комиссия'), ('СООПР', 'СООПР'), ('Женское', 'Женское'), ('Мужское', 'Мужское'), ('Занято', 'Занято'), ('Пусто', 'Пусто')], db_index=True, max_length=30, null=True)),
                ('faculty', models.CharField(blank=True, db_index=True, max_length=10, null=True)),
                ('form_studies', models.CharField(blank=True, choices=[('БЮДЖЕТ', 'Бюджет'), ('ПВЗ', 'ПВЗ')], db_index=True, max_length=10, null=True)),
                ('group', models.CharField(blank=True, db_index=True, max_length=10, null=True)),
                ('sex', models.CharField(blank=True, choices=[('М', 'Мужской'), ('Ж', 'Женский')], db_index=True, max_length=2, null=True)),
                ('mobile_number', models.BigIntegerField(blank=True, db_index=True, null=True)),
                ('fluorography', models.BooleanField(db_index=True, default=False)),
                ('pediculosis', models.BooleanField(db_index=True, default=False)),
                ('contract_number', models.CharField(blank=True, db_index=True, max_length=15, null=True)),
                ('agreement_date', models.DateField(blank=True, null=True)),
                ('registration', models.DateField(blank=True, null=True)),
                ('citizenship', models.CharField(blank=True, db_index=True, max_length=20, null=True)),
                ('date_of_birthday', models.DateField(blank=True, null=True)),
                ('place_of_birthday', models.CharField(blank=True, db_index=True, max_length=70, null=True)),
                ('document_number', models.CharField(blank=True, db_index=True, max_length=20, null=True)),
                ('authority', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_issue', models.DateField(blank=True, null=True)),
                ('notation', models.TextField(blank=True, db_index=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='hostel.Room', to_field='room_numb')),
            ],
            options={
                'verbose_name': 'historical student',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
