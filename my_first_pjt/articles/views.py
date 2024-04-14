from django.shortcuts import render
from .models import Article

# Create your views here.

# 함수형 뷰
# 클래스형 뷰 - 하나의 클래스 안에 여러 개 함수, 다른 클래스도 상속 가능 (코드를 좀 더 줄일 수 있겠구나)
def index(request) :
  # 이 함수로 요청이 들어왔을 때 할 일들을 적어주자
  return render(request, "index.html")

def data_throw(request) :
  return render(request, "data_throw.html")

def data_catch(request) :
  print("\n\n<<<<<<<<<<")
  print(request)
  print(request.GET)
  message = request.GET.get("message")
  context = {"message" : message}
  return render(request, "data_catch.html", context)

def articles(request) :
  articles = Article.objects.all()
  context = {
    "articles" : articles
  }
  return render(request, "articles.html", context)

def new(request) :
  return render(request, "new.html")

def create(request) :
  # 새로운 아티클 DB에 저장하기
  title = request.POST.get("title")
  content = request.POST.get("content")
  
  # 새로운 아티클 저장
  Article.objects.create(title = title, content=content)
  return render(request, "create.html")