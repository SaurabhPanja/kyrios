# Generated by Django 3.0.5 on 2020-12-04 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jugaad', '0004_auto_20201204_1234'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
            ],
        ),
    ]
