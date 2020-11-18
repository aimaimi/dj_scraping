from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
  name = f"scrapoo {datetime.today()}"
  html = f"<h1>Hello {name}</h1>"
  return HttpResponse(html)
