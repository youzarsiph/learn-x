# Generated by Django 4.2.4 on 2024-02-07 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_description_alter_project_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, help_text='Project image', null=True, upload_to='images/projects/'),
        ),
    ]
