# Generated by Django 4.1 on 2023-03-29 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0005_rename_answer_cards_answers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flashcards',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
                ('box_number', models.IntegerField(default=1)),
            ],
        ),
        migrations.DeleteModel(
            name='Cards',
        ),
    ]
