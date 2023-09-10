# Generated by Django 4.2.5 on 2023-09-05 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_alter_course_academicyear_alter_course_semester_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='department',
            field=models.CharField(choices=[('Cse(Regular)', 'Cse(R)'), ('Cse(Honorous)', 'Cse(H)'), ('Cs&It', 'CsIt')], max_length=50),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='designation',
            field=models.CharField(choices=[('prof', 'professor'), ('Assoc proff', 'Assoc proff'), ('Asst proff', 'Asst proff')], max_length=20),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=20),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='qualification',
            field=models.CharField(choices=[('Btech', 'Btech'), ('Mtech', 'Mtech'), ('PHD', 'PHD')], max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(choices=[('Cse(Regular)', 'Cse(R)'), ('Cse(Honorous)', 'Cse(H)'), ('Cs&It', 'CsIt')], max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='program',
            field=models.CharField(choices=[('Btech', 'Btech'), ('Mtech', 'Mtech')], max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='semester',
            field=models.CharField(choices=[('odd', 'odd'), ('Even', 'Even')], max_length=20),
        ),
    ]