# Generated by Django 4.0.2 on 2022-02-13 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0007_numberplate_videofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numberplate',
            name='img',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
