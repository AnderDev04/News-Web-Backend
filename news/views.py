from rest_framework.views import APIView
from .models import News, Category
from .serializers import NewsSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework import status

class NewsListView(APIView):
    def get(self, request):
        news = News.objects.filter(is_deleted=False)
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsListViewFull(APIView):
    def get(self, request):
        news = News.objects.filter(is_deleted=True)
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class NewsDetailView(APIView):
    def get(self, request, pk):
        news = News.objects.get(id=pk)
        serializer = NewsSerializer(news)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        try:
            news = News.objects.get(id=pk)
        except News.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = NewsSerializer(news, data=request.data, partial=True)
        
        # Validar los datos
        if serializer.is_valid():
            # Guardar los datos validados
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # Si los datos no son válidos, devolver los errores
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        news = News.objects.get(id=pk)
        news.is_deleted = True
        news.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
 
    
class DeleteNewsAPI(APIView):
    def delete(self, request, pk):
        news = News.objects.get(id=pk)
        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class CategoryListView(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class CategoryDetailView(APIView):
    def get(self, request, pk):
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        category = Category.objects.get(id=pk)
        category.is_deleted = False
        category.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class DeleteCategoryAPI(APIView):
    def delete(self, request, pk):
        news = News.objects.get(id=pk)
        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    