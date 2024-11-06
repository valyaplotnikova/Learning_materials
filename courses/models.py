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
        on_delete=models.CASCADE,
        verbose_name='модули курса',
        related_name='modules'
    )

    def __str__(self):
        return f'{self.course_name} - {self.description}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
        # ordering = ['course_name', 'speakers', 'company', 'drugs']
