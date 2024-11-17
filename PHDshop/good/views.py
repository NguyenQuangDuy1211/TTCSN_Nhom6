from pstats import Stats

from django.shortcuts import get_object_or_404
from .models import Good
from .serializer import GoodSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class GoodListView(APIView):
    def get(self):
        queryset = Good.objects.all()
        serializer_objects = GoodSerializer(queryset, many= True)
        return Response(serializer_objects.data, status = status.HTTP_200_OK)

class GetListViewFromCategory(APIView):
   def get(self,request, category_id):
       queryset = Good.objects.filter(category__id = category_id)
       seralizer_objects = GoodSerializer(queryset, many = True)
       return Response(seralizer_objects.data, status = status.HTTP_200_OK)

class GetListViewFromBrand(APIView):
    def get(self,request, brand_id):
        queryset = Good.objects.filter(brand__id = brand_id)
        serializer_objects = GoodSerializer(queryset, many = True)
        return Response(serializer_objects.data, status = status.HTTP_200_OK)

class GetDetailFromID(APIView):
    def get(self, pk):
        good = get_object_or_404(Good, pk=pk)
        serializer = GoodSerializer(good)
        return Response(serializer.data, status = status.HTTP_200_OK)


