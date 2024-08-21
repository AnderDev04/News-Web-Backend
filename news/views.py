from rest_framework.views import APIView
from .models import News
from .serializers import NewsSerializer
from rest_framework.response import Response
from rest_framework import status

class NewsListView(APIView):
    def get(self, request):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class NewsDetailView(APIView):
    def get(self, request, pk):
        news = News.objects.get(id=pk)
        serializer = NewsSerializer(news)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        news = News.objects.get(id=pk)
        serializer = NewsSerializer(news, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        news = News.objects.get(id=pk)
        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def delete_logica(self, request, pk):
        news = News.objects.get(id=pk)
        news.is_active = False
        news.save()
        return Response(status=status.HTTP_204_NO_CONTENT)