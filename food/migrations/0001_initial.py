# Generated by Django 4.0.2 on 2022-02-09 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=200)),
                ('itemprice', models.IntegerField()),
                ('itemdesc', models.CharField(max_length=200)),
            ],
        ),
    ]