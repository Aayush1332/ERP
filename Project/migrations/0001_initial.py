# Generated by Django 4.1.4 on 2023-03-26 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('projectdate', models.DateField()),
                ('cat', models.CharField(max_length=100)),
            ],
        ),
    ]
