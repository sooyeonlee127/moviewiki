from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, profile_image, nickname, password=None):
        print("userManager1")
        if email is None:
            raise ValueError('Users must have a email')
        if not nickname:
            raise ValueError('Users must have a nickname')
        if not profile_image:
            raise ValueError('Users must have a profile_image')

        user = self.model(
        email=self.normalize_email(email),
        nickname=nickname,
        profile_image=profile_image,
        )
        print("userManager2")
        user.set_password(password)
        user.save(using=self._db)
        print("userManager3")
        return user

    def create_superuser(self, email, profile_image, nickname, password=None):
        print("createSuperuser-- 1111")
        user = self.create_user(
            email,
            nickname=nickname,
            profile_image=profile_image,
            password=password,
        )
        print("createSuperuser-- 12222")
        user.is_admin = True
        user.save(using=self._db)
        print("createSuperuser-- 3333")
        return user



class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True, 
    )
    nickname = models.CharField(max_length=15)
    profile_image = models.ImageField(null = True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email








'''
from django.db import models
from django.contrib.auth.models import ( AbstractBaseUser, BaseUserManager, PermissionsMixin )
import jwt
from datetime import datetime, timedelta
from django.conf import settings

class UserManager(BaseUserManager):
    #  Django 의 Custom User 의 Field 저장을 위해서는 UserManager 재정의가 필수이다.
    def create_user(self, `username`, email, password=None):
        """Create and return a `User` with an email, username and password."""
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 로그인 시 USERNAME_FIELD 로 사용할 필드 설정
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    @property
    def token(self):
        """
        Allows us to get a user's token by calling `user.token` instead of
        `user.generate_jwt_token().

        The `@property` decorator above makes this possible. `token` is called
        a "dynamic property".
        """
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 60 days into the future.
        """
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%S'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')
'''