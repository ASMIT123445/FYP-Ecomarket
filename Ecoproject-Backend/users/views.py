from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from.serializers import RegisterSerializer
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


class RegisterSellerView(APIView):
    def post(self, request):
        data = request.data.copy()
        data['role'] = 'seller'
        serializer = RegisterSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Seller registered successfully"}, status=201)

        return Response(serializer.errors, status=400)

class RegisterUserView(APIView):
    def post(self, request):
        data = request.data.copy()
        data['role'] = 'customer'
        serializer = RegisterSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=201)

        return Response(serializer.errors, status=400)

    
class LoginView(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = User.objects.filter(username = username).first()
        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                "access_token" : str(refresh.access_token),
                "refresh_token" : str(refresh)
            })
        return Response({"message" : "Invalid credential"}, status=status.HTTP_400_BAD_REQUEST)
    
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        serializer = RegisterSerializer(user)
        return Response(serializer.data)