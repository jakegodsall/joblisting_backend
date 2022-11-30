# Generated by Django 4.1.3 on 2022-11-30 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobslist_app', '0006_alter_company_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='contract',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='jobslist_app.contract'),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='level',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='jobslist_app.level'),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='role',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='jobslist_app.role'),
        ),
    ]
