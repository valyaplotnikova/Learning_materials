from rest_framework import serializers

from courses.models import Course
from modules.serializers import ModuleSerializer


class CourseSerializer(serializers.ModelSerializer):

    modules_count = serializers.SerializerMethodField()
    modules = ModuleSerializer(many=True, read_only=True)
    tags = serializers.SerializerMethodField()

    def get_modules_count(self, obj):
        return obj.modules.count()

    def get_tags(selfself, obj):
        return obj.modules.tags.all()

    class Meta:
        model = Course
        fields = ['course_name', 'modules_count', 'tags']
