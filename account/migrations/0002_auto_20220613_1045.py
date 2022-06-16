# Generated by Django 3.1.6 on 2022-06-13 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='department',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('select', 'select'), ('male', 'male'), ('female', 'female')], default='select', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='matric_no',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]