# Generated by Django 3.1.4 on 2021-01-08 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='long_description',
        ),
        migrations.RemoveField(
            model_name='job',
            name='short_description',
        ),
        migrations.AddField(
            model_name='job',
            name='amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='category',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='currency',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='customer',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='from_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='gulf_exp',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='max_exp',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='min_exp',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='qualification_type',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='salary_type',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='specialization',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='status',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='task_id',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='to_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='vacancies',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='working_hours',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]