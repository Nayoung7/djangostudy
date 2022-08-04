from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# view 내부의 index 함수에서는 Hello, world 라는 응답을 클라이언트에게 전달해줌