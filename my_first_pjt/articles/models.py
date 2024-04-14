from django.db import models

# Create your models here.
# 테이블로 만들거야~ 라고만 적어주었으므로 migrate 과정 필요
class Article(models.Model):
  title = models.CharField(max_length=50)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)  # 생성(추가될 때 ~)
  updated_at = models.DateTimeField(auto_now=True)      # 수정

  def __str__(self) :
    return self.title
