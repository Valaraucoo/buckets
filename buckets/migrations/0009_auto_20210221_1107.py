# Generated by Django 3.1.6 on 2021-02-21 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buckets', '0008_auto_20210221_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bucketfile',
            name='filename',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
    ]
