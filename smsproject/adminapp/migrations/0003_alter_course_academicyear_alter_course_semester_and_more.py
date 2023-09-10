# Generated by Django 4.2.5 on 2023-09-05 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_alter_course_department_alter_course_semester_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='academicyear',
            field=models.CharField(choices=[('2023-24', '2023-24'), ('2022-23', '2022-23')], max_length=20),
        ),
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.CharField(choices=[('odd', 'odd'), ('Even', 'Even')], max_length=10),
        ),
        migrations.AlterField(
            model_name='course',
            name='year',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')]),
        ),
    ]
