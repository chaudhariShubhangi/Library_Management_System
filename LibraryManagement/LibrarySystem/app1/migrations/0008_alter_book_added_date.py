# Generated by Django 4.0.3 on 2022-09-21 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_alter_book_added_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='added_date',
            field=models.DateField(null=True),
        ),
    ]
