from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password

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

        # 이미 있는 id라면 다시 입력해야 함
        try: 
            find = User.objects.filter(user_id=user_id)        
        except User.DoesNotExist:
            data = {'error': "이미 존재하는 아이디입니다."}
            return render(request, 'user/register.html', data)
        # else:
            # if password != find.password:
            #     return render(request, 'user/login.html')
            # else:
            #     return HttpResponseRedirect('/blog')
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
    if request.method == 'GET':
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        userid = request.POST['username']
        password = request.POST['password']

        try: 
            find = User.objects.get(user_id=userid)        
        except (User.DoesNotExist):
            return render(request, 'user/login.html')
        else:
            if password != find.password:
                return render(request, 'user/login.html')
            else:
                return HttpResponseRedirect('/blog')
