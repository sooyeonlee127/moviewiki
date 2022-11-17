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