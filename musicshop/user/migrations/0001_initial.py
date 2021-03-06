# Generated by Django 3.2.5 on 2021-07-15 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=20)),
                ('company', models.CharField(blank=True, max_length=80, null=True)),
                ('address', models.CharField(blank=True, max_length=70, null=True)),
                ('city', models.CharField(blank=True, max_length=40, null=True)),
                ('state', models.CharField(blank=True, max_length=40, null=True)),
                ('country', models.CharField(blank=True, max_length=40, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('phone', models.CharField(blank=True, max_length=13, null=True)),
                ('fax', models.CharField(blank=True, max_length=24, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('support_rep_id', models.IntegerField()),
            ],
        ),
    ]
