# Generated by Django 4.1.1 on 2022-11-28 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobslist_app', '0002_remove_joboffer_languages_joboffer_languages'),
    ]

    operations = [
        migrations.AddField(
            model_name='joboffer',
            name='tools',
            field=models.ManyToManyField(to='jobslist_app.tools'),
        ),
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
    ]