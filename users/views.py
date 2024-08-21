from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .utils import get_tokens_for_user

class LoginView(APIView):
    def post(self, request):
        if 'username' not in request.data or 'password' not in request.data:
            return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        
        username = request.data['username']
        password = request.data['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            user_data = UserSerializer(user).data
            auth_data = get_tokens_for_user(user)
            return Response({'user': user_data, **auth_data}, status=status.HTTP_200_OK)
        
        # Si la autenticación falla, retornar un error
        return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'msg': 'Successfully Logged out'}, status=status.HTTP_200_OK)
