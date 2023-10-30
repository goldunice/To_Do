# Generated by Django 4.2.6 on 2023-10-30 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.PositiveSmallIntegerField()),
                ('course', models.PositiveSmallIntegerField()),
                ('student_number', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('detail', models.TextField(blank=True, null=True)),
                ('isDone', models.BooleanField()),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.student')),
            ],
        ),
    ]
