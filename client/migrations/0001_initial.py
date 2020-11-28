# Generated by Django 3.1 on 2020-11-28 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('primary_contact', models.IntegerField()),
                ('secondary_contact', models.IntegerField()),
                ('address', models.TextField()),
                ('pin', models.IntegerField()),
                ('image', models.ImageField(upload_to='client/')),
                ('idproof', models.ImageField(upload_to='client/id')),
                ('password', models.CharField(max_length=50)),
                ('confirm_password', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'clientdetail',
            },
        ),
        migrations.CreateModel(
            name='ClientInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('primary_contact', models.IntegerField()),
                ('secondary_contact', models.IntegerField()),
                ('address', models.TextField()),
                ('pin', models.IntegerField()),
                ('image', models.ImageField(upload_to='client/')),
                ('idproof', models.ImageField(upload_to='client/id')),
                ('password', models.CharField(max_length=50)),
                ('confirm_password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('roll', models.IntegerField()),
            ],
            options={
                'db_table': 'detail',
            },
        ),
    ]
