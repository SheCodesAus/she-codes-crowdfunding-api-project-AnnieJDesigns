# Generated by Django 4.1.5 on 2023-01-29 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_charity_abn'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='charity_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='charity_abn',
            field=models.IntegerField(default=0),
        ),
    ]
