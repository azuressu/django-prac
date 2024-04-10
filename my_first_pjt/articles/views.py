from django.shortcuts import render

# Create your views here.

# 함수형 뷰
# 클래스형 뷰 - 하나의 클래스 안에 여러 개 함수, 다른 클래스도 상속 가능 (코드를 좀 더 줄일 수 있겠구나)
def index(request) :
  # 이 함수로 요청이 들어왔을 때 할 일들을 적어주자
  return render(request, "index.html")

def users(request) :
  return render(request, "users.html")

def hello(request) :
  name = "수연"
  tags = ["java", "spring", "html", "css"]
  books = ["백설공주", "신데렐라", "어린왕자", "잠자는 숲속의 공주"]
  context = {
    "name" : name,
    "tags" : tags,
    "books" : books,
  }
  return render(request, "hello.html", context)

def data_throw(request) :
  return render(request, "data_throw.html")

def data_catch(request) :
  print("\n\n<<<<<<<<<<")
  print(request)
  print(request.GET)
  message = request.GET.get("message")
  context = {"message" : message}
  return render(request, "data_catch.html", context)