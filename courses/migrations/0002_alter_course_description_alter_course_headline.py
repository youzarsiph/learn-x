# Generated by Django 4.2.4 on 2024-02-07 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(db_index=True, help_text='Course description', max_length=1024),
        ),
        migrations.AlterField(
            model_name='course',
            name='headline',
            field=models.CharField(db_index=True, help_text='Course headline', max_length=512),
        ),
    ]
