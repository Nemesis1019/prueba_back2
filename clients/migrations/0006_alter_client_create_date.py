# Generated by Django 4.2.2 on 2023-06-07 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_alter_client_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='create_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]