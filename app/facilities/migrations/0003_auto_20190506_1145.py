# Generated by Django 2.2.1 on 2019-05-06 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facilities', '0002_auto_20190506_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='REFINE_ZIP_CD',
            field=models.IntegerField(null=True, verbose_name='소재지우편번호'),
        ),
    ]
