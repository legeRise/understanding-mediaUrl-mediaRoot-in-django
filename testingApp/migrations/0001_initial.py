# Generated by Django 4.2.9 on 2024-02-10 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
