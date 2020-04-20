# Generated by Django 3.0 on 2020-04-04 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime', models.CharField(max_length=200)),
                ('summary', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Anime',
            },
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('skill', models.CharField(max_length=200)),
                ('power', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('slug', models.CharField(default=1, max_length=200)),
                ('anime', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.Anime', verbose_name='Anime')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('slug', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Genre',
            },
        ),
        migrations.DeleteModel(
            name='Player',
        ),
        migrations.AddField(
            model_name='anime',
            name='genre',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.Genre', verbose_name='Genre'),
        ),
    ]
