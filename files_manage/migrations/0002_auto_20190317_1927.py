# Generated by Django 2.1.7 on 2019-03-17 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files_manage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filemodel',
            old_name='myfile',
            new_name='file',
        ),
        migrations.AddField(
            model_name='filemodel',
            name='name',
            field=models.CharField(default='a', max_length=255),
            preserve_default=False,
        ),
    ]