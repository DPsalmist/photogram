# Generated by Django 3.1.6 on 2022-06-13 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0005_auto_20210219_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='price',
            field=models.CharField(blank=True, default=100, max_length=200),
        ),
    ]
