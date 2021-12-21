
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import Group
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


class ClientView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ClientSerializer

    def get_queryset(self):
        queryset = User.objects.filter(is_client=True)
        return queryset


class EditClientView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    lookup_fields = ['pk']
    queryset = User.objects.all()
    serializer_class = ClientSerializer


class UserView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        queryset = User.objects.filter(is_client=False)
        return queryset


class EditUserView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    lookup_fields = ['pk']
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer


class GroupsView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = GroupsSerializer
    queryset = Group.objects.all()


class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            print(token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print("ok")
            return Response(status=status.HTTP_400_BAD_REQUEST)


class testLogin(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        request.user.last_login = timezone.now()
        request.user.save(update_fields=["last_login"])
        return Response({"name": request.user.user_name})


class StaffLogin(TokenObtainPairView):
    serializer_class = StaffTokenObtainPairSerializer


class ClientLogin(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class ClientInfo(generics.ListCreateAPIView):
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
