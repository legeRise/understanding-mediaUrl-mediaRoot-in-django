# Generated by Django 4.2.9 on 2024-02-11 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testingApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='my_image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
