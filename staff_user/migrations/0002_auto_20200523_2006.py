# Generated by Django 2.1.4 on 2020-05-23 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='hours',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('h_name', models.CharField(max_length=32, null=True)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(auto_now=True)),
                ('hours_today', models.CharField(default=0, max_length=16)),
                ('record_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('s_name', models.CharField(max_length=32)),
                ('s_mobilenumber', models.CharField(max_length=64, unique=True)),
                ('s_isworking', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='staff_user',
        ),
    ]
