from rest_framework import generics

from modules.models import Module, Course
from modules.serializers import ModuleSerializer, ModuleGetSerializer, CourseGetSerializer, CourseSerializer


class ModuleCreateAPIView(generics.CreateAPIView):
    serializer_class = ModuleGetSerializer


class ModuleListAPIView(generics.ListAPIView):
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()


class ModuleRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ModuleGetSerializer
    queryset = Module.objects.all()


class ModuleUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ModuleGetSerializer
    queryset = Module.objects.all()


class ModuleDestroyAPIView(generics.DestroyAPIView):
    queryset = Module.objects.all()


class CourseCreateAPIView(generics.CreateAPIView):
    serializer_class = CourseGetSerializer


class CourseListAPIView(generics.ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CourseGetSerializer
    queryset = Course.objects.all()


class CourseUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CourseGetSerializer
    queryset = Course.objects.all()


class CourseDestroyAPIView(generics.DestroyAPIView):
    queryset = Course.objects.all()

