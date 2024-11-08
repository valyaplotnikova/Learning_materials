from django.db import models
from config.settings import AUTH_USER_MODEL


NULLABLE = {'blank': True, 'null': True}


class Video(models.Model):
    video_name = models.CharField(
        max_length=100,
        verbose_name='название видео'
    )
    video_file = models.FileField(
        upload_to='modules/video',
        verbose_name='видео'
    )
    video_watched = models.BooleanField(
        default=False,
        **NULLABLE,
        verbose_name='видео просмотрено'
    )

    class Meta:
        verbose_name = 'видео'
        verbose_name_plural = 'видео'


class Test(models.Model):
    test = models.FileField(
        upload_to='modules/tests/',
        verbose_name='тест',
        **NULLABLE
    )
    test_is_done = models.BooleanField(
        default=False,
        verbose_name='отметка о прохождении теста'
    )

    class Meta:
        verbose_name = 'тест'
        verbose_name_plural = 'тесты'


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
    module = models.ForeignKey(
        'Module',
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name='модуль'
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
        return self.tag_name

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
    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
        verbose_name='видео',
        **NULLABLE
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
    video = models.OneToOneField(
        Video,
        on_delete=models.SET_NULL,
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
        related_name='speakers',
        **NULLABLE
    )
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        **NULLABLE,
        verbose_name='тесты модуля',
        related_name='tests'
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
    course = models.ForeignKey(
        'Course',
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name='курс'
    )
    certificate = models.OneToOneField(
        'Certificate',
        on_delete=models.CASCADE,
        verbose_name='сертификат модуля',
        **NULLABLE
    )

    def __str__(self):
        return f'{self.name} - {self.description}'

    class Meta:
        verbose_name = 'модуль'
        verbose_name_plural = 'модули'
        ordering = ['name']


class Certificate(models.Model):

    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='владелец сертификата'
    )
    is_cert = models.BooleanField(
        default=False,
        verbose_name='отметка о выдаче сертификата'
    )

    def __str__(self):
        return f'{self.owner} - {self.is_cert}'

    class Meta:
        verbose_name = 'сертификат'
        verbose_name_plural = 'сертификаты'


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
    certificate = models.OneToOneField(
        Certificate,
        on_delete=models.CASCADE,
        verbose_name='сертификат курса',
        **NULLABLE
    )

    def __str__(self):
        return f'{self.course_name} - {self.description}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
