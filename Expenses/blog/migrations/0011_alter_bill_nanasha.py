# Generated by Django 4.2.5 on 2024-03-28 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_bill_nanasha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='nanasha',
            field=models.FloatField(blank=True),
        ),
    ]
