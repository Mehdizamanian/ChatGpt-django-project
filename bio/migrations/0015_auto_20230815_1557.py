# Generated by Django 3.2 on 2023-08-15 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0014_alter_resume_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='loc_src_map',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=230),
        ),
    ]