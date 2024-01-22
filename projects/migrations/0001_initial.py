# Generated by Django 4.2.4 on 2024-01-22 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Project image', upload_to='images/projects/')),
                ('name', models.CharField(db_index=True, help_text='Project name', max_length=32, unique=True)),
                ('description', models.CharField(help_text='Project description', max_length=256)),
                ('content', models.TextField(help_text='Project content')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Last update')),
            ],
        ),
    ]