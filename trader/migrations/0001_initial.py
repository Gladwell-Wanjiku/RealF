# Generated by Django 5.0.6 on 2024-07-06 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('traders_id', models.IntegerField()),
                ('traders_fullname', models.CharField(max_length=40)),
                ('traders_email', models.EmailField(max_length=254)),
                ('traders_location', models.TextField()),
                ('traders_password', models.PositiveBigIntegerField()),
            ],
        ),
    ]
