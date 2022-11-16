from django.db import transaction
from rest_framework import serializers
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from dj_rest_auth.registration.serializers import RegisterSerializer



class RegisterSerializer(RegisterSerializer):
    # 기본 설정 필드: username, password, email
    nickname = serializers.CharField(max_length=15)
    # 추가 설정 필드: profile_image
    profile_image = serializers.ImageField(use_url=True)
    
    @transaction.atomic
    def save(self, request):
        print("save제발되랴ㅏ1")
        user = super().save(request)
        print("save제발되랴ㅏ2")
        user.nickname = self.data.get('nickname')
        user.profile_image = self.data.get('profile_image')
        user.save()
        print("save제발되랴ㅏ3")
        return user
