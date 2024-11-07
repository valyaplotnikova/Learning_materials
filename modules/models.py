from django.db import models

from courses.models import Course

NULLABLE = {'blank': True, 'null': True}


class Test(models.Model):
    test = models.FileField(
        upload_to='modules/tests/',
        verbose_name='тест'
    )
    test_is_done = models.BooleanField(
        default=False,
        verbose_name='отметка о прохождении теста'
    )


class File(models.Model):
    file_name = models.CharField(
        max_length=150,
        verbose_name='название файла',
        **NULLABLE
    )
    file_type = models.CharField(
        max_length=100,
        verbose_name='тип файла',
        **NULLABLE
    )
    file = models.FileField(
        upload_to='modules/files',
        verbose_name='файл'
    )
    file_is_done = models.BooleanField(
        default=False,
        verbose_name='отметка о скачивании файла'
    )

    class Meta:
        verbose_name = 'файл'
        verbose_name_plural = 'файлы'


class Speaker(models.Model):

    full_name = models.CharField(
        max_length=150,
        verbose_name='полное имя'
    )
    photo = models.ImageField(
        upload_to='modules/photos/',
        verbose_name='фото'
    )
    post = models.TextField(
        verbose_name='должность'
    )

    def __str__(self):
        return f'{self.full_name}, {self.post}'

    class Meta:
        verbose_name = 'спикер'
        verbose_name_plural = 'спикеры'
        ordering = ["full_name", "post"]


class Drug(models.Model):

    drag_name = models.CharField(
        max_length=150,
        verbose_name='название препарата'
    )
    photo = models.ImageField(
        upload_to='modules/photos/',
        verbose_name='фото препарата'
    )

    def __str__(self):
        return self.drag_name

    class Meta:
        verbose_name = 'препарат'
        verbose_name_plural = 'препараты'


class Company(models.Model):

    company_name = models.CharField(
        max_length=150,
        verbose_name='название компании'
    )

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'компания'
        verbose_name_plural = 'компании'


class Tag(models.Model):
    tag_name = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'тэг'
        verbose_name_plural = 'тэги'


class Timecode(models.Model):

    time = models.TimeField(
        verbose_name='временная метка'
    )
    description = models.TextField(
        verbose_name='описание'
    )

    def __str__(self):
        return f'{self.time} - {self.description}'

    class Meta:
        verbose_name = 'таймкод'
        verbose_name_plural = 'таймкоды'


class Module(models.Model):

    name = models.CharField(
        max_length=150,
        verbose_name='название модуля'
    )
    description = models.TextField(
        verbose_name='описание модуля'
    )
    video = models.FileField(
        upload_to='modules/videos/',
        verbose_name='видео модуля',
        **NULLABLE
    )
    photo = models.ImageField(
        upload_to='modules/photos/',
        verbose_name='фото модуля',
        **NULLABLE
    )
    timecodes = models.ManyToManyField(
        Timecode,
        **NULLABLE,
        related_name='timecodes'
    )
    tags = models.ManyToManyField(
        Tag,
        **NULLABLE,
        related_name='tags'
    )
    speakers = models.ManyToManyField(
        Speaker,
        verbose_name='спикеры модуля',
        related_name='speakers'
    )
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        verbose_name='материалы модуля',
        related_name='materials'
    )
    drugs = models.ForeignKey(
        Drug,
        on_delete=models.SET_NULL,
        verbose_name='препараты модуля',
        **NULLABLE,
        related_name='drugs'
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        verbose_name='компания-спонсор модуля',
        **NULLABLE
    )
    disclaimer = models.TextField(
        verbose_name='дисклеймер',
        **NULLABLE
    )
    is_in_course = models.BooleanField(
        default=False,
        verbose_name='модуль в составе курса',
        **NULLABLE
    )
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, **NULLABLE, verbose_name='курс')

    def __str__(self):
        return f'{self.name} - {self.description}'

    class Meta:
        verbose_name = 'модуль'
        verbose_name_plural = 'модули'
        # ordering = ['name', 'speakers', 'company', 'drugs']
