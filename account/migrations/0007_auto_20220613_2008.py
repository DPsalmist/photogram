# Generated by Django 3.1.6 on 2022-06-13 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20220613_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='matric_no',
            field=models.CharField(blank=True, default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='static/photos/media/default.jpeg', upload_to='users/%Y/%m/%d/'),
        ),
    ]
