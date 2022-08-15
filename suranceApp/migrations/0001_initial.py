# Generated by Django 4.1 on 2022-08-15 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('goalMoney', models.IntegerField()),
                ('savedMoney', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.IntegerField()),
                ('date', models.DateField()),
                ('category', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]
