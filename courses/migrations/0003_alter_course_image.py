# Generated by Django 4.2.4 on 2024-02-07 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_course_description_alter_course_headline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, help_text='Course image', null=True, upload_to='images/courses/'),
        ),
    ]
