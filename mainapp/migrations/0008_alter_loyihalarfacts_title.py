# Generated by Django 4.1.2 on 2022-10-11 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_alter_coursefacts_title_alter_teacherfacts_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loyihalarfacts',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
