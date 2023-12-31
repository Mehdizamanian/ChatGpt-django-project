# Generated by Django 3.2 on 2023-08-14 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0007_social'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contact',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='home',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='resume',
            name='picowner',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='resume',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
