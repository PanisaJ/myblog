# Generated by Django 3.0.3 on 2020-02-20 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20200219_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(default='picture/no_image.png', upload_to='media'),
        ),
    ]
