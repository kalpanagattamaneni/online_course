# Generated by Django 3.1.7 on 2021-03-23 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_is_mvp'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_mode',
            field=models.CharField(default=False, max_length=50),
        ),
    ]