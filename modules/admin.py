from django.contrib import admin

from modules.models import Video, Test, File, Speaker, Drug, Company, Tag, Module, Course, Timecode


@admin.register(Timecode)
class TimecodeAdmin(admin.ModelAdmin):
    list_display = ('time', 'description',)
    search_fields = ['description']

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('video_name', 'video_file', 'video_watched')
    list_display_links = ('video_name', 'video_file',)
    ordering = ['video_name']
    search_fields = ['video_name']
    list_editable = ('video_watched',)


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('test', )
    list_display_links = ('test', )
    ordering = ['test']
    search_fields = ['test']


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'file_type', 'file', 'module', 'file_is_done')
    list_display_links = ('file_name', 'file_type', 'file', 'module')
    ordering = ['file_name', 'file_type', 'module']
    search_fields = ['file_name', 'file_type', 'module']
    list_editable = ('file_is_done', )


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'photo', 'post',)
    list_display_links = ('full_name', )
    ordering = ['full_name', 'post']
    search_fields = ['full_name']


@admin.register(Drug)
class DrugAdmin(admin.ModelAdmin):
    list_display = ('drag_name', 'photo',)
    list_display_links = ('drag_name',)
    ordering = ['drag_name']
    search_fields = ['drag_name']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', )
    list_display_links = ('company_name',)
    ordering = ['company_name']
    search_fields = ['company_name']


@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('tag_name', )
    list_display_links = ('tag_name',)
    ordering = ['tag_name']
    search_fields = ['tag_name']


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'video', 'photo', 'test', 'is_in_course', 'drugs',
                    'company', 'disclaimer', 'course')
    list_display_links = ('name', 'description', 'video', 'photo', 'test', 'drugs',
                          'company', 'disclaimer', 'course')
    ordering = ['name', 'company']
    search_fields = ['name', 'company']
    list_editable = ('is_in_course',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'course_name', 'preview', 'description',)
    list_display_links = ('id', 'course_name', 'preview', 'description',)
    ordering = ['course_name']
    search_fields = ['course_name']
