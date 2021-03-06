# Generated by Django 2.0 on 2018-09-14 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BottomData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('price', models.CharField(max_length=512)),
                ('color', models.CharField(max_length=512)),
                ('sizes', models.CharField(max_length=512)),
                ('description', models.CharField(max_length=512)),
                ('specs', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='ExclusivesData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('price', models.CharField(max_length=512)),
            ],
        ),
    ]
