# Generated by Django 4.2.4 on 2023-08-18 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
