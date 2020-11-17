from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  name = "scrapoo"
  html = f"<h1>Hello {name}</h1>"
  return HttpResponse(html)
