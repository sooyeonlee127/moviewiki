from django.shortcuts import render
from .serializers import UserDetailsSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .models import User

# Create your views here.
@api_view(['PUT'])
def update(request):
    if request.method == 'PUT':
        print(request.user)
        user = User.objects.get(email=request.user.email)
        serializer = UserDetailsSerializer(user, data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)