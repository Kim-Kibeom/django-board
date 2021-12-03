from django.db import models

# Create your models here.
class User(models.Model):
    user_id     = models.CharField(max_length=100, verbose_name='id')
    email       = models.EmailField(max_length=100, verbose_name='이메일')
    password    = models.CharField(max_length=100, verbose_name='비밀번호')
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name='가입 날짜')
    updated_at  = models.DateTimeField(auto_now=True, verbose_name='수정 날짜')

    def __str__(self):
        return self.user_id