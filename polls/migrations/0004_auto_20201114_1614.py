# Generated by Django 3.1.3 on 2020-11-14 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_question_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='no_of_options',
        ),
        migrations.AddField(
            model_name='question',
            name='option1',
            field=models.CharField(default='Option 1', max_length=200),
        ),
        migrations.AddField(
            model_name='question',
            name='option2',
            field=models.CharField(default='Option 2', max_length=200),
        ),
        migrations.AddField(
            model_name='question',
            name='option3',
            field=models.CharField(default='Option 3', max_length=200),
        ),
        migrations.AddField(
            model_name='question',
            name='option4',
            field=models.CharField(default='Option 4', max_length=200),
        ),
    ]
