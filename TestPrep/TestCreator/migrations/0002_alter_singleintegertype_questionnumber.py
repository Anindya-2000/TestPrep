# Generated by Django 3.2 on 2021-04-25 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestCreator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singleintegertype',
            name='QuestionNumber',
            field=models.IntegerField(null=True),
        ),
    ]
