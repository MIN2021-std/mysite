from django.db import models

import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    id = 1
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        # 현재 시간 - 하루 전날의 시간 => 어제의 시간을 반환
        # 어제 이후에 발행이 된 데이터가 반환됨.


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE) # 하나의 Q에 여러개를 갖고 있음 즉, 1:N
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# on_delete -> 질문이 삭제되면 선택 모델의 질문도 삭제하겠다