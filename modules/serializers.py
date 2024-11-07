from rest_framework import serializers

from modules.models import Module


class ModuleGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Module
        fields = '__all__'


class ModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Module
        fields = ['tags', 'name', 'materials']
