# Generated by Django 4.2.3 on 2023-08-01 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_expense_date_added'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Event',
        ),
    ]
