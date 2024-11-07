from rest_framework import generics

from modules.models import Module
from modules.serializers import ModuleSerializer, ModuleGetSerializer


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
