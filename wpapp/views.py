from django.shortcuts import render
from .serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView,DestroyAPIView,UpdateAPIView, GenericAPIView
from .models import *
from rest_framework.response import Response
from rest_framework.reverse import reverse


class ApiRoot(GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'list': reverse('list_permit', request=request),
            'create-list': reverse('create_permit', request=request),
            'list-activity': reverse('list_activity', request=request),
            'create-activity': reverse('create_activity', request=request)

        })


# Create your views here.
class CreatePermitView(CreateAPIView):
    queryset = WorkPermit.objects.all()
    serializer_class = WorkPermitSerializer


class ListPermitView(ListAPIView):
    queryset = WorkPermit.objects.all()
    serializer_class = WorkPermitSerializer

class UpdatePermitView(UpdateAPIView):
    queryset = WorkPermit.objects.all()
    serializer_class = WorkPermitSerializer

class DeletePermitView(DestroyAPIView):
    queryset = WorkPermit.objects.all()
    serializer_class = WorkPermitSerializer




'''
---------------------------------------------------------------------------------
'''



class CreateExamplePermitView(CreateAPIView):
    queryset = WorkpermitExample.objects.all()
    serializer_class = ExampleWorkPermitSerializer


class ListExamplePermitView(ListAPIView):
    queryset = WorkpermitExample.objects.all()
    serializer_class = ExampleWorkPermitSerializer

class UpdateExamplePermitView(UpdateAPIView):
    queryset = WorkpermitExample.objects.all()
    serializer_class = ExampleWorkPermitSerializer

class DeleteExamplePermitView(DestroyAPIView):
    queryset = WorkpermitExample.objects.all()
    serializer_class = ExampleWorkPermitSerializer