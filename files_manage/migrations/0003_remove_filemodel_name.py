# Generated by Django 2.1.7 on 2019-03-17 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files_manage', '0002_auto_20190317_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filemodel',
            name='name',
        ),
    ]