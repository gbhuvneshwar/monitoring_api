# Generated by Django 2.2 on 2021-02-09 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benisonTech_monitoring_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devices',
            name='memory_utilization',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
