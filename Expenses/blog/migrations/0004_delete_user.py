# Generated by Django 4.2.5 on 2024-03-28 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_user_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user',
        ),
    ]
