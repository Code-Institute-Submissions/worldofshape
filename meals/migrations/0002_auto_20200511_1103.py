# Generated by Django 3.0.4 on 2020-05-11 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='description2',
            new_name='full_description',
        ),
        migrations.RemoveField(
            model_name='meal',
            name='description3',
        ),
        migrations.RemoveField(
            model_name='meal',
            name='name_id',
        ),
        migrations.AlterField(
            model_name='meal',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='meal',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='meal',
            name='name2',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='mealprogram',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='mealprogram',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]