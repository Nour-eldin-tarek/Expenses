# Generated by Django 4.2.5 on 2024-03-28 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_bill_nanasha'),
    ]

    operations = [
        migrations.CreateModel(
            name='expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=15)),
                ('product_name', models.CharField(max_length=15)),
                ('product_price', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='bill',
            name='descrip',
            field=models.TextField(default='مشتريات'),
        ),
    ]
