# Generated by Django 3.2.9 on 2021-11-27 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationshed',
            name='services',
            field=models.ManyToManyField(to='reservation.Services'),
        ),
    ]
