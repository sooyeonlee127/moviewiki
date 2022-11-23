# from django.shortcuts import render
# from .serializers import RegisterSerializer
# from rest_framework.decorators import permission_classes
# from rest_framework.permissions import IsAuthenticated
# from django.conf import settings 
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status

# # Create your views here.
# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])
# def update(request):
#     if request.method == 'PUT':
#         print(request.data)
#         serializer = RegisterSerializer(settings.AUTH_USER_MODEL, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             print(request.data)
#             serializer.save()
#             return Response(serializer.data)
        
        
        
#     '''
#     @login_required
#     @require_http_methods(['GET', 'POST'])
#     def update(request):
#         if request.method == 'POST':
#             form = CustomUserChangeForm(request.POST, instance=request.user)
#             # form = CustomUserChangeForm(data=request.POST, instance=request.user)
#             if form.is_valid():
#                 form.save()
#                 return redirect('articles:index')
#         else:
#             form = CustomUserChangeForm(instance=request.user)
#         context = {
#             'form': form,
#         }
#         return render(request, 'accounts/update.html', context)


    
#     '''


# from rest_framework import serializers
# from dj_rest_auth.serializers import UserDetailsSerializer
# from .models import UserProfile


# class UserProfileSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = UserProfile
#         fields = '__all__'
        
# class UserSerializer(UserDetailsSerializer):
#     profile = UserProfileSerializer(source="userprofile")
    
#     class Meta(UserDetailsSerializer.Meta):
#         fields = UserDetailsSerializer.Meta.fields + ('profile',)
        
#     def update(self, instance, validated_data):
#         userprofile_serializer = self.fields['profile']
#         userprofile_instance = instance.userprofile
#         userprofile_data = validated_data.pop('userprofile', {})
#         # to access the 'company_name' field in here
#         # company_name = userprofile_data.get('company_name')
#         # update the userprofile fields
#         userprofile_serializer.update(userprofile_instance, userprofile_data)
#         instance = super().update(instance, validated_data)
#         return instance