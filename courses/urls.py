from django.urls import path

from courses.apps import CoursesConfig
from courses.views import CourseListAPIView

app_name = CoursesConfig.name

urlpatterns = [
    path('', CourseListAPIView.as_view(), )

]