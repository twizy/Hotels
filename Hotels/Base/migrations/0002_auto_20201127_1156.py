# Generated by Django 2.2.5 on 2020-11-27 09:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='hotel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='hotel', to='Base.Hotels'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hotels',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
