# Generated by Django 3.2.9 on 2021-12-27 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0003_alter_donation_transaction_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
    ]
