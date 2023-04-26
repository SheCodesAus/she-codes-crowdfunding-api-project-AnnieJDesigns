# Generated by Django 4.1.5 on 2023-01-29 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customuser_charity_name_alter_customuser_charity_abn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='charity_abn',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='charity_name',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
