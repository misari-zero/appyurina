# Generated by Django 3.2.7 on 2021-10-30 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0008_alter_project_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
    ]
