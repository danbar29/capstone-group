# Generated by Django 5.1.1 on 2024-11-04 00:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_transaction_description_alter_transaction_fund'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donor_name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('transaction_type', models.CharField(choices=[('Credit', 'Credit'), ('Debit', 'Debit')], max_length=10)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('goal_end_date', models.DateField()),
                ('goal_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donor_name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('transaction_type', models.CharField(choices=[('Credit', 'Credit'), ('Debit', 'Debit')], max_length=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='main.project')),
            ],
        ),
    ]
