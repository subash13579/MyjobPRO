# Generated by Django 2.2.10 on 2021-01-25 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_auto_20210121_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='alternate_contact',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='imo_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='pincode',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
