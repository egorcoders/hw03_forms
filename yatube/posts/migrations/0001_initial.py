# Generated by Django 2.2.6 on 2022-08-17 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название тематической группы', max_length=200, verbose_name='Название группы')),
                ('slug', models.SlugField(help_text='Укажите порядковый номер группы', unique=True, verbose_name='Номер группы')),
                ('description', models.TextField(help_text='Добавьте текст описания группы', verbose_name='Описание группы')),
            ],
            options={
                'verbose_name': 'Группа статей',
                'verbose_name_plural': 'Группы статей',
                'ordering': ('-title',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Введите текст статьи', verbose_name='Текст статьи')),
                ('pub_date', models.DateTimeField(auto_now_add=True, help_text='Укажите дату публикации', verbose_name='Дата публикации')),
                ('author', models.ForeignKey(help_text='Укажите автора статьи', on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='Автор статьи')),
                ('group', models.ForeignKey(blank=True, help_text='Выберите тематическую группу в выпадающем списке по желанию', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='posts.Group', verbose_name='Группа статей')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'ordering': ('-pub_date',),
            },
        ),
    ]
