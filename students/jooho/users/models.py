from django.db import models

class User(models.Model):
    name        = models.CharField(max_length=20)
    email       = models.EmailField(max_length=200,unique=True)
    password    = models.CharField(max_length=200)#암호화되어 저장될것을 대비하여 글자제한 크게 설정
    phone_number= models.CharField(max_length=50)#국제전화번호 고려하여 글자제한 크게  설정
    birthday    = models.DateField(blank=True,null=True)#생일 정보를 입력하고 싶지않은 이용자는 빈칸으로 사용가능
    gender      = models.CharField(max_length=20,blank=True,null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class meta:
        db_table = 'users'



