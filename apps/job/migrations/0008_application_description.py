# Generated by Django 2.2.10 on 2021-04-23 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
