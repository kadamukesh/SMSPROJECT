# Generated by Django 4.2.5 on 2023-09-07 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0008_student_aadharno'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='credits',
            field=models.FloatField(default='0'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='ltps',
            field=models.CharField(default='0-0-0-0', max_length=10),
            preserve_default=False,
        ),
    ]
