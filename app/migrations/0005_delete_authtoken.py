# Generated by Django 3.2.4 on 2021-06-16 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_user_last_login'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AuthToken',
        ),
    ]
