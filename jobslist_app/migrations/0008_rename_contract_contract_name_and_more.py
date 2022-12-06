# Generated by Django 4.1.4 on 2022-12-06 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobslist_app', '0007_contract_level_role_alter_joboffer_contract_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contract',
            old_name='contract',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobslist_app.contract'),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobslist_app.level'),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobslist_app.location'),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobslist_app.role'),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='tools',
            field=models.ManyToManyField(blank=True, to='jobslist_app.tools'),
        ),
    ]
