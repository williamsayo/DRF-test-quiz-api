# Generated by Django 3.2.14 on 2022-07-07 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0006_auto_20220706_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(default='Django', max_length=50),
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(default='Django', max_length=50, unique=True),
        ),
    ]