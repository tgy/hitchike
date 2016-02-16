# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-16 23:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import hitcount.models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('content_html', models.TextField(blank=True, editable=False)),
                ('content', models.TextField()),
                ('validated', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('content_html', models.TextField(blank=True, editable=False)),
                ('content', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['create_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('content_html', models.TextField(blank=True, editable=False)),
                ('content', models.TextField()),
                ('title', models.CharField(max_length=140, verbose_name='Question')),
                ('slug_title', models.SlugField(max_length=140, unique=True)),
                ('answered', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
                ('answers', models.ManyToManyField(related_name='question_answers', to='qa.Answer')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-create_at'],
                'abstract': False,
            },
            bases=(models.Model, hitcount.models.HitCountMixin),
        ),
        migrations.AddField(
            model_name='answer',
            name='comments',
            field=models.ManyToManyField(related_name='answer_comments', to='qa.Comment'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
