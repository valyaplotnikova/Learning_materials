# Generated by Django 5.1.3 on 2024-11-06 16:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('modules', '0003_alter_module_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=150, verbose_name='название курса')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='courses/previews/', verbose_name='изображение курса')),
                ('description', models.TextField(verbose_name='описание курса')),
                ('modules', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='modules.module', verbose_name='модули курса')),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
            },
        ),
    ]