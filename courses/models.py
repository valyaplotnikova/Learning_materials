from django.db import models

from modules.models import NULLABLE, Module, Speaker, Materials, Drug


class Course(models.Model):
    course_name = models.CharField(
        max_length=150,
        verbose_name='название курса'
    )
    preview = models.ImageField(
        upload_to='courses/previews/',
        verbose_name='изображение курса',
        **NULLABLE
    )
    description = models.TextField(
        verbose_name='описание курса'
    )
    modules = models.ForeignKey(
        Module,
        on_delete=models.SET_NULL,
        verbose_name='модули курса',
        related_name='modules'
    )
    speakers = models.ManyToManyField(
        Speaker,
        verbose_name='спикеры курса',
        related_name='speakers'
    )
    materials = models.ForeignKey(
        Materials,
        on_delete=models.SET_NULL,
        verbose_name='материалы курса',
        related_name='materials'
    )
    drugs = models.ForeignKey(
        Drug,
        on_delete=models.SET_NULL,
        verbose_name='препараты курса',
        **NULLABLE,
        related_name='drugs'
    )
    disclaimer = models.TextField(
        verbose_name='дисклеймер',
        **NULLABLE
    )
