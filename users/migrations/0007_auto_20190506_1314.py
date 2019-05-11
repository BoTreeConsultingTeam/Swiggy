# Generated by Django 2.2.1 on 2019-05-06 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190506_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='city_and_state.City'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='city_and_state.State'),
        ),
    ]