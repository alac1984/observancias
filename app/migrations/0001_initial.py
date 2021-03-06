# Generated by Django 3.1.7 on 2021-04-28 13:36

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
            name='Podcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateField(auto_now=True, verbose_name='Modified')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', models.CharField(max_length=250)),
                ('hero', models.FileField(upload_to='')),
                ('url', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateField(auto_now=True, verbose_name='Modified')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('hero', models.FileField(upload_to='')),
                ('description', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateField(auto_now=True, verbose_name='Modified')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('name', models.CharField(max_length=80, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('body', models.TextField(max_length=1100, verbose_name='Mensagem')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='app.comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app.post')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
