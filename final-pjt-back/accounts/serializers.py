from django.db import transaction
from rest_framework import serializers
# from allauth.account.adapter import get_adapter
# from allauth.account.utils import setup_user_email
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model

class RegisterSerializer(RegisterSerializer):
    # 기본 설정 필드: username, password, email
    username = None
    nickname = serializers.CharField(max_length=15)
    # 추가 설정 필드: profile_image
    # profile_image = serializers.ImageField(use_url=True, required=False)
    
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
        read_only_fields = ('USERNAME_FIELD','nickname', 'profile_image')
