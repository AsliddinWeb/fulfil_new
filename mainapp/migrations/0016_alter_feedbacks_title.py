# Generated by Django 4.1.2 on 2022-10-14 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_alter_feedbacks_tartib_raqami'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbacks',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]