# from django.contrib import admin
#
# from modules.models import Materials, Speaker, Drug, Company, Tags,
#
#
# @admin.register(Materials)
# class MaterialsAdmin(admin.ModelAdmin):
#     list_display = ('test', 'presentation', 'file',)
#     list_display_links = ('test', 'presentation', 'file',)
#
#
# @admin.register(Speaker)
# class SpeakerAdmin(admin.ModelAdmin):
#     list_display = ('full_name', 'photo', 'post',)
#     list_display_links = ('full_name', )
#     ordering = ['full_name', 'post']
#     search_fields = ['full_name']
#
#
# @admin.register(Drug)
# class DrugAdmin(admin.ModelAdmin):
#     list_display = ('drag_name', 'photo',)
#     list_display_links = ('drag_name',)
#     ordering = ['drag_name']
#     search_fields = ['drag_name']
#
#
# @admin.register(Company)
# class CompanyAdmin(admin.ModelAdmin):
#     list_display = ('company_name', )
#     list_display_links = ('company_name',)
#     ordering = ['company_name']
#     search_fields = ['company_name']
#
#
# @admin.register(Tags)
# class TagsAdmin(admin.ModelAdmin):
#     list_display = ('tag', )
#     list_display_links = ('tag',)
#     ordering = ['tag']
#     search_fields = ['tag']


# @admin.register(Module)
# class ModuleAdmin(admin.ModelAdmin):
#     list_display = ('time', 'description')
#     list_display_links = ('time', 'description',)
#     ordering = ['time']
#     search_fields = ['description']