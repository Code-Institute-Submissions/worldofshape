# Generated by Django 3.0.4 on 2020-05-11 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_auto_20200511_1103'),
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meallineitem',
            name='meal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meals.Meal'),
        ),
    ]