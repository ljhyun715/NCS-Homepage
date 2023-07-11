from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager, PermissionsMixin
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, username, email, type, address, tel, fax, password=None):
        if not username:
            raise ValueError('user name')
        if not email:
            raise ValueError('user email')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            type=type,
            address=address,
            tel=tel,
            fax=fax
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, type, address, tel, fax, password):
        user = self.create_user(
            username=username,
            email=self.normalize_email(email),
            type=type,
            address=address,
            tel=tel,
            fax=fax,
            password = password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPES = (
        ('individual', '개인회원'),
        ('company', '기업회원'),
        ('quality', '품질책임자'),
        ('technical', '기술책임자'),
        ('staff', '실무자'),
        ('admin', '총관리자')
    )
    type = models.CharField(max_length=100, choices=USER_TYPES)
    email = models.EmailField(max_length=200, unique=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    address = models.CharField(max_length=400)
    tel = models.CharField(max_length=200)
    fax = models.IntegerField()

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['type', 'username', 'address', 'tel', 'fax']

    def __str__(self):
        return self.username


def has_perm(self, perm, obj=None):
    return True


def has_module_perms(self, app_label):
    return True


@property
def is_staff(self):
    return self.is_admin
