# Generated by Django 2.2.5 on 2020-12-02 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HotelApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotels',
            name='place',
        ),
        migrations.AddField(
            model_name='hotels',
            name='province',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='provinc', to='HotelApp.Provinces'),
            preserve_default=False,
        ),
    ]
