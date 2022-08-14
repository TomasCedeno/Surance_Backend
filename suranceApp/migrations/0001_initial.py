# Generated by Django 4.1 on 2022-08-14 03:46

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
    ]