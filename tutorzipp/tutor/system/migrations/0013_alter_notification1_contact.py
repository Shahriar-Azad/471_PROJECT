# Generated by Django 5.0.3 on 2024-04-19 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0012_notification1_stdname_last'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification1',
            name='contact',
            field=models.IntegerField(null=True),
        ),
    ]