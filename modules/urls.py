from django.urls import path

from modules.apps import ModulsConfig
from modules.views import ModuleCreateAPIView, ModuleListAPIView, ModuleRetrieveAPIView, ModuleUpdateAPIView, \
    ModuleDestroyAPIView

app_name = ModulsConfig.name

urlpatterns = [
    path('create/', ModuleCreateAPIView.as_view(), name='module-create'),
    path('', ModuleListAPIView.as_view(), name='module-list'),
    path('get/<int:pk>/', ModuleRetrieveAPIView.as_view(), name='module-get'),
    path('update/<int:pk>/', ModuleUpdateAPIView.as_view(), name='module-update'),
    path('delete/<int:pk>/', ModuleDestroyAPIView.as_view(), name='module-delete'),
]
