# Generated by Django 2.2.3 on 2019-07-06 00:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categorys'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.RemoveField(
            model_name='course',
            name='name',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='name',
        ),
        migrations.AddField(
            model_name='category',
            name='title',
            field=models.CharField(default='', max_length=50, verbose_name='Title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='student',
            field=models.ManyToManyField(blank=True, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='course',
            name='title',
            field=models.CharField(default='', max_length=50, verbose_name='Title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lesson',
            name='title',
            field=models.CharField(default='', max_length=50, verbose_name='Title'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ManyToManyField(blank=True, related_name='teacher', to='courses.Teacher', verbose_name='Teacher'),
        ),
    ]
