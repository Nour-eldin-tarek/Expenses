# Generated by Django 4.2.5 on 2024-03-28 23:24

import blog.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0017_remove_bill_user_id_delete_expenses_delete_person_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrip', models.TextField(default='مشتريات')),
                ('nanasha', models.FloatField(blank=True, null=True)),
                ('join_date', models.DateTimeField(auto_now_add=True)),
                ('nameOfBuyer', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=15)),
                ('l_name', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('bassword', models.CharField(max_length=20, validators=[blog.models.validate_min_length])),
                ('join_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.user')),
            ],
        ),
        migrations.CreateModel(
            name='expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=15)),
                ('product_name', models.CharField(max_length=15)),
                ('product_price', models.FloatField()),
                ('bill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.bill')),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.user'),
        ),
    ]
