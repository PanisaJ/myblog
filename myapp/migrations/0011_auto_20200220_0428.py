# Generated by Django 3.0.3 on 2020-02-20 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20200220_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(default='no_image.png', upload_to='image'),
        ),
    ]
