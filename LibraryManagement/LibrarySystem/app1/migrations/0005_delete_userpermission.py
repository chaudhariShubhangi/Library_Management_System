# Generated by Django 4.0.3 on 2022-09-20 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_user_user_role'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserPermission',
        ),
    ]
