# Generated by Django 3.2.14 on 2022-10-30 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_question_quiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(default='Unknown-quiz', on_delete=django.db.models.deletion.CASCADE, to='app.quiz'),
        ),
    ]
