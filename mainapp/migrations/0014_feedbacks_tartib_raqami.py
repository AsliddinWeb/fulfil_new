# Generated by Django 4.1.2 on 2022-10-14 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_alter_learninglist_tartib_raqami'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbacks',
            name='tartib_raqami',
            field=models.SmallIntegerField(default=0),
        ),
    ]