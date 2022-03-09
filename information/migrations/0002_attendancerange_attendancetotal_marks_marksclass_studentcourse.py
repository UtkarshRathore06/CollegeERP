# Generated by Django 3.1.7 on 2021-05-15 06:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceRange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='information.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='information.student')),
            ],
            options={
                'verbose_name_plural': 'Marks',
                'unique_together': {('student', 'course')},
            },
        ),
        migrations.CreateModel(
            name='MarksClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Internal test 1', 'Internal test 1'), ('Internal test 2', 'Internal test 2'), ('Internal test 3', 'Internal test 3'), ('Event 1', 'Event 1'), ('Event 2', 'Event 2'), ('Semester End Exam', 'Semester End Exam')], default='Internal test 1', max_length=50)),
                ('status', models.BooleanField(default='False')),
                ('assign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='information.assign')),
            ],
            options={
                'unique_together': {('assign', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Internal test 1', 'Internal test 1'), ('Internal test 2', 'Internal test 2'), ('Internal test 3', 'Internal test 3'), ('Event 1', 'Event 1'), ('Event 2', 'Event 2'), ('Semester End Exam', 'Semester End Exam')], default='Internal test 1', max_length=50)),
                ('marks1', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('studentcourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='information.studentcourse')),
            ],
            options={
                'unique_together': {('studentcourse', 'name')},
            },
        ),
        migrations.CreateModel(
            name='AttendanceTotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='information.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='information.student')),
            ],
            options={
                'unique_together': {('student', 'course')},
            },
        ),
    ]
