from django.contrib import admin

from modules.models import Materials, Speaker, Drug, Company, Tags, Timecode, Module

admin.site.register(Materials)
admin.site.register(Speaker)
admin.site.register(Drug)
admin.site.register(Company)
admin.site.register(Tags)
admin.site.register(Timecode)
admin.site.register(Module)
