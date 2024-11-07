from rest_framework import serializers

from courses.models import Course
from modules.serializers import ModuleSerializer


class CourseSerializer(serializers.ModelSerializer):

    modules_count = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()

    @staticmethod
    def get_modules_count(obj):
        return obj.modules.count()

    @staticmethod
    def get_tags(obj):
        tag_list = []
        for module in obj.modules.all():
            for tag in module.tags.all():
                tag_list.append(tag.tag)
        return set(tag_list)

    class Meta:
        model = Course
        fields = ['course_name', 'preview', 'modules_count', 'tags']


class CourseGetSerializer(serializers.ModelSerializer):

    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['course_name', 'preview', 'description', 'modules']
