# Generated by Django 5.1.2 on 2024-11-02 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosextra',
            name='avatar',
            field=models.ImageField(blank=True, default='media/default_avatar.jpg', null=True, upload_to='avatares'),
        ),
    ]
