# Generated by Django 5.1.1 on 2024-10-22 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('Credit', 'Credit'), ('Debit', 'Debit')], max_length=6)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fund', models.CharField(choices=[('general', 'General Fund'), ('specific', 'Specific Fund')], max_length=8)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
