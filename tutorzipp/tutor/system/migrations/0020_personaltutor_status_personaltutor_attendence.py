# Generated by Django 4.2.5 on 2024-04-21 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0019_remove_attendence_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaltutor',
            name='Status',
            field=models.CharField(default='Due', max_length=100),
        ),
        migrations.AddField(
            model_name='personaltutor',
            name='attendence',
            field=models.IntegerField(default=0),
        ),
    ]
