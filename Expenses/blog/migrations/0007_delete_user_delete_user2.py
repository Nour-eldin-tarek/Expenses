# Generated by Django 4.2.5 on 2024-03-28 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_user2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user',
        ),
        migrations.DeleteModel(
            name='user2',
        ),
    ]
