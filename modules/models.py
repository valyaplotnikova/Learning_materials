from django.db import models
from timecode.fields import TimecodeField


NULLABLE = {'blanck': True, 'null': True}


class Materials(models.Model):
    test = models.FileField(upload_to='modules/tests/', verbose_name='тест')
    presentation = models.FileField(upload_to='modules/presentations/', verbose_name='презентация', **NULLABLE)

    class Meta:
        verbose_name = 'материалы'
        verbose_name_plural = 'материалы'


class Speaker(models.Model):

    full_name = models.CharField(max_length=150, verbose_name='полное имя')
    photo = models.ImageField(upload_to='modules/photos/', verbose_name='фото')
    post = models.TextField(verbose_name='должность')

    def __str__(self):
        return f'{self.full_name}, {self.post}'

    class Meta:
        verbose_name = 'спикер'
        verbose_name_plural = 'спикеры'
        ordering = ["full_name", "post"]


class Drug(models.Model):

    drag_name = models.CharField(max_length=150, verbose_name='название препарата')
    photo = models.ImageField(upload_to='modules/photos/', verbose_name='фото препарата')

    def __str__(self):
        return self.drag_name

    class Meta:
        verbose_name = 'препарат'
        verbose_name_plural = 'препараты'


class Pharmcompany(models.Model):

    company_name = models.CharField(max_length=150, verbose_name='название компании')

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'компания'
        verbose_name_plural = 'компании'


class Tags(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'тэг'
        verbose_name_plural = 'тэги'


class Timecode(models.Model):

    timecode = TimecodeField

    def __str__(self):
        return self.timecode

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
    timecode = models.ManyToManyField(
        Timecode,
        **NULLABLE,
        related_name='timecodes'
    )
    tags = models.ManyToManyField(
        Tags,
        **NULLABLE,
        related_name='tags'
    )
    speakers = models.ManyToManyField(
        Speaker,
        verbose_name='спикеры модуля',
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
    company = models.ForeignKey(
        Pharmcompany,
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
