from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, CreateUserSerializer


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def user_current(request):
    """
    Determine the current user by their token, and return their data
    """
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAdminUser])
def user_list(APIView):
    """
    List all users
    """
    return Response(
        UserSerializer(user).data for user in User.objects.all()
    )


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def create_user(request):
    """
    Create a new user
    """
    serializer = CreateUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
