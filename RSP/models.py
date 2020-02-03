from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.contrib.auth.models import UserManager as DefaultUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager


class Weapons(models.Model):
    WEAPON_CHOICES = (
        ('가위', "가위"),
        ('바위', "바위"),
        ('보', "보"),
    )
    weapon=models.CharField(max_length=255, null=True, blank=True, choices=WEAPON_CHOICES)

    def __str__(self):
        return self.weapon




class FriendRequest(models.Model):
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="to_user", null=True, blank=True)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="from_user",null=True, blank=True)
    to_user_rsp = models.ForeignKey(Weapons, on_delete=models.CASCADE, related_name='to_user_rsp', null=True, blank=True)
    from_user_rsp = models.ForeignKey(Weapons, on_delete=models.CASCADE, related_name='from_user_rsp', null=True, blank=True)
    result = models.CharField(max_length=255, null=True, blank=True)
    to_user_result = models.CharField(max_length=255, null=True, blank=True)
    from_user_result = models.CharField(max_length=255, null=True, blank=True)
    from_user_num=models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.to_user}에게 {self.from_user}가"

# 오류 : 'UserManager' object has no attribute 'get_or_create_google_user'
# class UserManager(BaseUserManager):  #DefaultUserManager
#     def get_or_create_google_user(self, user_pk):  #extra_data
#         user = User.objects.get(pk=user_pk)
#         user.username = user.first_name  #user.extra['first_name']
#         user.save()
#
#         return user
#
# #
# # class User(AbstractUser):
# #     objects = UserManager()
