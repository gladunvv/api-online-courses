# Generated by Django 2.2.3 on 2019-07-10 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='student',
            field=models.BooleanField(blank=True, verbose_name='Student'),
        ),
    ]