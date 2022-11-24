# from django.db import transaction
from rest_framework import serializers
# from allauth.account.adapter import get_adapter
# from allauth.account.utils import setup_user_email
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
# from .models import UserProfile

class RegisterSerializer(RegisterSerializer):
    # 기본 설정 필드: username, password, email
    username = None
    nickname = serializers.CharField(max_length=15)
    # 추가 설정 필드: profile_image
    profile_image = serializers.ImageField(required=False)
    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['nickname'] = self.validated_data.get('nickname', '')
        data['profile_image'] = self.validated_data.get('profile_image', '')
        return data
    
    # @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.nickname = self.data.get('nickname')
        user.profile_image = self.data.get('profile_image')
        user.save()
        return user


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        extra_fields = []
        # see https://github.com/iMerica/dj-rest-auth/issues/181
        # UserModel.XYZ causing attribute error while importing other
        # classes from `serializers.py`. So, we need to check whether the auth model has
        # the attribute or not
        UserModel = get_user_model()
        if hasattr(UserModel, 'USERNAME_FIELD'):
            extra_fields.append(UserModel.USERNAME_FIELD)
        if hasattr(UserModel, 'nickname'):
            extra_fields.append('nickname')
        if hasattr(UserModel, 'profile_image'):
            extra_fields.append('profile_image')
        model = UserModel
        fields = ('pk', *extra_fields)
        read_only_fields = ('email',)








# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = ('nickname','profile_image',)
        
# class UserSerializer(UserDetailsSerializer):
#     profile = UserProfileSerializer(source="userprofile")
    
#     class Meta(UserDetailsSerializer.Meta):
#         fields = UserDetailsSerializer.Meta.fields + ('profile',)

    
#     def update(self, instance, validated_data):
#         # userprofile_serializer = self.fields['profile']
#         userprofile_instance = instance.userprofile
#         userprofile_data = validated_data.pop('userprofile', {})
#         # to access the 'company_name' field in here
#         # company_name = userprofile_data.get('company_name')
#         # update the userprofile fields
#         self.update(userprofile_instance, userprofile_data)
#         instance = super().update(instance, validated_data)
#         return instance
