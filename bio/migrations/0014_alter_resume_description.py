# Generated by Django 3.2 on 2023-08-15 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0013_alter_resume_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
