# Generated by Django 4.1.2 on 2022-10-11 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_coursefacts_coursename_feedbacks_imkoniyat_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursefacts',
            name='icon',
        ),
    ]
