# Generated by Django 4.0.4 on 2022-04-25 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=40)),
                ('continent', models.CharField(max_length=40, null=True)),
            ],
        ),
    ]