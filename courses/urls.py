from django.urls import path

from courses.apps import CoursesConfig
from courses.views import CourseListAPIView, CourseRetrieveAPIView, CourseUpdateAPIView, CourseDestroyAPIView, \
    CourseCreateAPIView

app_name = CoursesConfig.name

urlpatterns = [
    path('', CourseListAPIView.as_view(), name='course-list'),
    path('get/<int:pk>/', CourseRetrieveAPIView.as_view(), name='course-get'),
    path('update/<int:pk>/', CourseUpdateAPIView.as_view(), name='course-update'),
    path('delete/<int:pk>/', CourseDestroyAPIView.as_view(), name='course-delete'),
    path('create/', CourseCreateAPIView.as_view(), name='course-create'),
]
