# Generated by Django 3.1 on 2020-11-28 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_auto_20201128_1843'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClientInfo',
            new_name='ClientInformation',
        ),
        migrations.DeleteModel(
            name='ClientDetail',
        ),
        migrations.DeleteModel(
            name='detail',
        ),
        migrations.AlterModelTable(
            name='clientinformation',
            table='clientinformation',
        ),
    ]
