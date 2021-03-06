# Generated by Django 3.1.7 on 2021-03-22 07:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('instructors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('course_curriculum', models.TextField(blank=True)),
                ('main_image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('next_batch_start_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('is_mvp', models.BooleanField(default=False)),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='instructors.instructor')),
            ],
        ),
    ]
