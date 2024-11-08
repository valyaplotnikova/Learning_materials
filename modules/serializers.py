from rest_framework import serializers

from modules.models import Module, File, Course


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = ['file_name', 'file_type', 'file', 'file_is_done']


class ModuleGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Module
        fields = '__all__'


class ModuleSerializer(serializers.ModelSerializer):

    files = FileSerializer(many=True, read_only=True)
    files_count = serializers.SerializerMethodField()

    @staticmethod
    def get_files_count(obj):
        return obj.file_set.count()

    class Meta:
        model = Module
        fields = ['tags', 'name', 'test', 'files', 'files_count', 'certificate']


class CourseSerializer(serializers.ModelSerializer):

    modules_count = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()

    @staticmethod
    def get_modules_count(obj):
        return obj.module_set.count()

    @staticmethod
    def get_tags(obj):
        tag_list = []
        for module in obj.module_set.all():
            for tag in module.tags.all():
                tag_list.append(tag.tag_name)
        return set(tag_list)

    class Meta:
        model = Course
        fields = ['course_name', 'preview', 'modules_count', 'tags']


class CourseGetSerializer(serializers.ModelSerializer):

    modules = ModuleGetSerializer(source='module_set', many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['course_name', 'preview', 'description', 'modules', 'certificate']

