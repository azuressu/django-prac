from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def profile(request, username) :
  print("넘어온 유저네임은 \n\n\n")
  print(username)
  return HttpResponse("test")