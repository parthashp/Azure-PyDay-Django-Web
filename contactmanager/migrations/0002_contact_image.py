# Generated by Django 3.0.7 on 2020-06-22 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactmanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]