from rest_framework import generics

from courses.models import Course
from courses.serializers import CourseSerializer


class CourseCreateAPIView(generics.CreateAPIView):
    serializer_class = CourseSerializer


class CourseListAPIView(generics.ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseDestroyAPIView(generics.DestroyAPIView):
    queryset = Course.objects.all()
