from django.shortcuts import render
from rest_framework.views import APIView
from .models import employees
from rest_framework.response import Response
from rest_framework import  serializers
from .serializers import employeeSerializers

class employeeList(APIView):

    def get(self, request):
        data = employees.objects.all()
        serializer = employeeSerializers(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass


# Create your views here.
