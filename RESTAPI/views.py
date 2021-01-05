from django.shortcuts import render
from .models import categories,desserts
# Create your views here.
from rest_framework.response import  Response
from rest_framework.views import APIView
from .serializers import categoriesSerializer,dessertSerializer
from .models import categories,desserts
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser

class categoryDetail(APIView):
    def get(self,request):
        category = categories.objects.all()
        serializers = categoriesSerializer(category,many=True)
        return Response(serializers.data)

    def post(self,request):
        pass

    parser_class = (FileUploadParser,)

    def put(self, request, format=None):
        if 'file' not in request.data:
            raise ParseError("Empty content")

        f = request.data['file']

        file = categories.objects.create(image = f)

class dessertDetail(APIView):
    def get(self,request):
        dessert = desserts.objects.all()
        serializers = dessertSerializer(dessert,many=True)
        return Response(serializers.data)

    def post(self,request):
        pass

    def put(self, request, format=None):
        if 'file' not in request.data:
            raise ParseError("Empty content")

        f = request.data['file']

        file = desserts.objects.create(image=f)