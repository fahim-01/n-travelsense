# Generated by Django 3.1.1 on 2020-09-28 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customize', '0003_auto_20200928_0456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='desc',
            field=models.CharField(max_length=6000),
        ),
    ]
