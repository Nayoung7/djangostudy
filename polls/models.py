import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
# 두 테이블의 관계 : 하나의 Question에 여러개의 Choice를 갖는 관계이므로 일-대-다(one-to-many)
class Question(models.Model):
    # question_text : 질문 내용, pub_date : 생성 날짜
    question_text = models.CharField(max_length=200)    # question_text 의 데이터형 : 문자 타입(길이 200)
    pub_date = models.DateTimeField('date published')   # pub_date 의 데이터형 : 시간 타입

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        # 버그 수정 전
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1) # 현재시간에서 하루를 뺀 즉 어제이후에 발행된 데이터 리턴됨

        # 버그 수정 후 : question 생성날짜가 미래로 넘어가지 않도록 현재날짜를 두고 최근 기준을 하루로 둔것
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now



class Choice(models.Model):
    # question : 선택지에 해당하는 질문, choice_text : 선택지, votes = 투표 수
    question = models.ForeignKey(Question, on_delete=models.CASCADE)    # 데이터형 : 외래키(Question을 참조)
    choice_text = models.CharField(max_length=200)  # 데이터형 : 문자 타입(길이 200)
    votes = models.IntegerField(default=0)  # 데이터형 : 숫자 타입

    def __str__(self):
        return self.choice_text


