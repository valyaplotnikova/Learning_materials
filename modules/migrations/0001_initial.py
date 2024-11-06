# Generated by Django 5.1.3 on 2024-11-06 16:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drag_name', models.CharField(max_length=150, verbose_name='название препарата')),
                ('photo', models.ImageField(upload_to='modules/photos/', verbose_name='фото препарата')),
            ],
            options={
                'verbose_name': 'препарат',
                'verbose_name_plural': 'препараты',
            },
        ),
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.FileField(upload_to='modules/tests/', verbose_name='тест')),
                ('presentation', models.FileField(blank=True, null=True, upload_to='modules/presentations/', verbose_name='презентация')),
                ('file', models.FileField(blank=True, null=True, upload_to='modules/files/', verbose_name='файл')),
            ],
            options={
                'verbose_name': 'материалы',
                'verbose_name_plural': 'материалы',
            },
        ),
        migrations.CreateModel(
            name='Pharmcompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=150, verbose_name='название компании')),
            ],
            options={
                'verbose_name': 'компания',
                'verbose_name_plural': 'компании',
            },
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150, verbose_name='полное имя')),
                ('photo', models.ImageField(upload_to='modules/photos/', verbose_name='фото')),
                ('post', models.TextField(verbose_name='должность')),
            ],
            options={
                'verbose_name': 'спикер',
                'verbose_name_plural': 'спикеры',
                'ordering': ['full_name', 'post'],
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'тэг',
                'verbose_name_plural': 'тэги',
            },
        ),
        migrations.CreateModel(
            name='Timecode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(verbose_name='временная метка')),
                ('description', models.TextField(verbose_name='описание модуля')),
            ],
            options={
                'verbose_name': 'таймкод',
                'verbose_name_plural': 'таймкоды',
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='название модуля')),
                ('description', models.TextField(verbose_name='описание модуля')),
                ('video', models.FileField(blank=True, null=True, upload_to='modules/videos/', verbose_name='видео модуля')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='modules/photos/', verbose_name='фото модуля')),
                ('disclaimer', models.TextField(blank=True, null=True, verbose_name='дисклеймер')),
                ('is_in_course', models.BooleanField(blank=True, default=False, null=True, verbose_name='модуль в составе курса')),
                ('drugs', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='drugs', to='modules.drug', verbose_name='препараты курса')),
                ('materials', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materials', to='modules.materials', verbose_name='материалы курса')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='modules.pharmcompany', verbose_name='компания-спонсор модуля')),
                ('speakers', models.ManyToManyField(related_name='speakers', to='modules.speaker', verbose_name='спикеры модуля')),
                ('tags', models.ManyToManyField(blank=True, null=True, related_name='tags', to='modules.tags')),
                ('timecodes', models.ManyToManyField(blank=True, null=True, related_name='timecodes', to='modules.timecode')),
            ],
        ),
    ]
