# Generated by Django 5.0.1 on 2024-01-22 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_student_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='file',
        ),
    ]
