# Generated by Django 5.1.4 on 2025-02-12 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_alter_user_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='registration',
            field=models.CharField(max_length=8, unique=True),
        ),
    ]
