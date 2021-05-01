# Generated by Django 3.2 on 2021-05-01 14:24

import TestCreator.models
import TestCreator.storage
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionPaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam', models.CharField(choices=[('JEE Mains', 'JEE Mains'), ('JEE Advanced', 'JEE Advanced'), ('KVPY', 'KVPY'), ('Bitsat', 'Bitsat')], max_length=100)),
                ('year', models.IntegerField(default=2020, null=True)),
                ('name', models.CharField(max_length=500, null=True)),
                ('total_number_of_questions', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userImage', models.ImageField(storage=TestCreator.storage.OverwriteStorage(), upload_to=TestCreator.models.create_path_user)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SingleIntegerType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ImageField(upload_to=TestCreator.models.create_path)),
                ('correct_answer', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=10)),
                ('QuestionNumber', models.IntegerField(null=True)),
                ('questionType', models.CharField(default='SingleIntegerType', max_length=100, null=True)),
                ('QuestionPaper', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='TestCreator.questionpaper')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionAttempts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Attempt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='TestCreator.attempt')),
            ],
        ),
        migrations.AddField(
            model_name='attempt',
            name='QuestionPaper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='TestCreator.questionpaper'),
        ),
        migrations.AddField(
            model_name='attempt',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
