# Generated by Django 4.1.7 on 2023-07-22 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0003_remove_meeting_members_meeting_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='is_finished',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
