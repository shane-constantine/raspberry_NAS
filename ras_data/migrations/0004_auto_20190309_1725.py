# Generated by Django 2.1.7 on 2019-03-09 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ras_data', '0003_auto_20190306_2013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ras_info',
            name='cpu_temperature',
        ),
        migrations.RemoveField(
            model_name='ras_info',
            name='cpu_useage',
        ),
        migrations.RemoveField(
            model_name='ras_info',
            name='data_page',
        ),
        migrations.RemoveField(
            model_name='ras_info',
            name='harddrive_useage',
        ),
        migrations.RemoveField(
            model_name='ras_info',
            name='humidity',
        ),
        migrations.RemoveField(
            model_name='ras_info',
            name='temperature',
        ),
        migrations.AddField(
            model_name='ras_info',
            name='CT',
            field=models.FloatField(default=0, max_length=255),
        ),
        migrations.AddField(
            model_name='ras_info',
            name='CU',
            field=models.FloatField(default=0, max_length=255),
        ),
        migrations.AddField(
            model_name='ras_info',
            name='DF',
            field=models.FloatField(default=0, max_length=255),
        ),
        migrations.AddField(
            model_name='ras_info',
            name='DP',
            field=models.FloatField(default=0, max_length=255),
        ),
        migrations.AddField(
            model_name='ras_info',
            name='DT',
            field=models.FloatField(default=0, max_length=255),
        ),
        migrations.AddField(
            model_name='ras_info',
            name='DU',
            field=models.FloatField(default=0, max_length=255),
        ),
        migrations.AddField(
            model_name='ras_info',
            name='H',
            field=models.FloatField(default=0, max_length=255),
        ),
        migrations.AddField(
            model_name='ras_info',
            name='RF',
            field=models.FloatField(default=0, max_length=255),
        ),
        migrations.AddField(
            model_name='ras_info',
            name='RP',
            field=models.FloatField(default=0, max_length=255),
        ),
        migrations.AddField(
            model_name='ras_info',
            name='RT',
            field=models.FloatField(default=0, max_length=255),
        ),
        migrations.AddField(
            model_name='ras_info',
            name='RU',
            field=models.FloatField(default=0, max_length=255),
        ),
        migrations.AddField(
            model_name='ras_info',
            name='T',
            field=models.FloatField(default=0, max_length=255),
        ),
    ]
