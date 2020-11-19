from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .forms import RequestForm
from django.views import generic
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

def get_yahooauction(url):
    res = requests.get(url)
    soup = bs(res.content, "html.parser")
    items = soup.findAll("li",class_="Product")

    return [
        {
            "title": item.find("a",class_="Product__titleLink").text.strip(),
            "url": item.find("a",class_="Product__titleLink").get("href"),
            "picture": item.find("img").get("src")
        }
        for item in items
    ]

class GetData(generic.FormView):
  template_name = "scrape/index.html"
  form_class = RequestForm

  def form_valid(self, form):
    form.save()
    url = form.cleaned_data["url"]
    result = get_yahooauction(url)
    context = {
      "url": url,
      "form": self.form_class,
      "name": f"scrapoo {datetime.today()}",
      "result": result
    }
    return render(
      self.request,
      self.template_name,
      context
    )

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["name"] = f"scrapoo {datetime.today()}"
    return context



def index(request):
  name = f"scrapoo {datetime.today()}"
  form = RequestForm()
  html = f"""
  <h1>Hello {name}</h1>
  <hr>
  {form}
  <hr>
  <button>Request</button>
  """
  return HttpResponse(html)
