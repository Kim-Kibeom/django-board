from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password

from .models import User

def register(request):
    if request.method == 'GET':
        # 로그인 진행
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        # 회원가입 진행
        user_id = request.POST['userid']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']

        # 비밀번호가 일치하지 않으면 
        # 에러문구 출력 후 다시 register로
        if password != re_password:
            data = {'error': '비밀번호가 일치하지 않습니다.'}
            return render(request, 'user/register.html', data)

        user = User(
            user_id = user_id,
            email = email,
            password = make_password(password),
        )
        user.save()

        return HttpResponseRedirect(reverse('user:login'))

def login(request):
    return render(request, 'user/login.html')