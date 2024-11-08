from django.urls import path

from modules.apps import ModulsConfig
from modules.views import ModuleCreateAPIView, ModuleListAPIView, ModuleRetrieveAPIView, ModuleUpdateAPIView, \
    ModuleDestroyAPIView, CourseListAPIView, CourseRetrieveAPIView, CourseUpdateAPIView, CourseDestroyAPIView, \
    CourseCreateAPIView

app_name = ModulsConfig.name

urlpatterns = [
    path('create/', ModuleCreateAPIView.as_view(), name='module-create'),
    path('', ModuleListAPIView.as_view(), name='module-list'),
    path('get/<int:pk>/', ModuleRetrieveAPIView.as_view(), name='module-get'),
    path('update/<int:pk>/', ModuleUpdateAPIView.as_view(), name='module-update'),
    path('delete/<int:pk>/', ModuleDestroyAPIView.as_view(), name='module-delete'),
    path('courses/', CourseListAPIView.as_view(), name='course-list'),
    path('courses_get/<int:pk>/', CourseRetrieveAPIView.as_view(), name='course-get'),
    path('courses_update/<int:pk>/', CourseUpdateAPIView.as_view(), name='course-update'),
    path('courses_delete/<int:pk>/', CourseDestroyAPIView.as_view(), name='course-delete'),
    path('courses_create/', CourseCreateAPIView.as_view(), name='course-create'),
]
