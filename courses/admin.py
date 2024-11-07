from django.contrib import admin

from courses.models import Course


# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ('id', 'course_name', 'preview', 'description', 'modules')
#     list_display_links = ('time', 'description',)
#     ordering = ['time']
#     search_fields = ['description']