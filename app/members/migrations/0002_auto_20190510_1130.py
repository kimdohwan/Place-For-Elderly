# Generated by Django 2.2.1 on 2019-05-10 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='likes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='facilities', to='facilities.Facility'),
        ),
    ]