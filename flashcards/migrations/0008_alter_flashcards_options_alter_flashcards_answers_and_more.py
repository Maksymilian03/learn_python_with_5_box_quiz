# Generated by Django 4.1 on 2023-04-08 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0007_rename_id_flashcards_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flashcards',
            options={'ordering': ['ID']},
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='answers',
            field=models.CharField(default='No answer', max_length=256),
        ),
        migrations.AlterModelTable(
            name='flashcards',
            table='flashcards_flashcards',
        ),
    ]
