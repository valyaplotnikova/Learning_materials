# Generated by Django 5.1.3 on 2024-11-07 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('modules', '0003_alter_module_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='modules',
        ),
        migrations.AddField(
            model_name='course',
            name='modules',
            field=models.ManyToManyField(related_name='modules', to='modules.module', verbose_name='модули курса'),
        ),
    ]
