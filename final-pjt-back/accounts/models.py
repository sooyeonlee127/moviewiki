from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# from django.contrib.auth.models import User


class UserManager(BaseUserManager):
    def create_user(self, email, profile_image, nickname, password=None):
        if email is None:
            raise ValueError('Users must have a email')
        if not nickname:
            raise ValueError('Users must have a nickname')
        # if not profile_image:
        #     raise ValueError('Users must have a profile_image')

        user = self.model(
        email=self.normalize_email(email),
        nickname=nickname,
        profile_image=profile_image,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, profile_image, nickname, password=None):
        user = self.create_user(
            email,
            nickname=nickname,
            profile_image=profile_image,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
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
    
    

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
#     # custom fields for user
#     nickname = models.CharField(max_length=15)
#     profile_image = models.ImageField(null = True)