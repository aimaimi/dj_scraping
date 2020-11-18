from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .forms import RequestForm
from django.views import generic


class GetData(generic.FormView):
  template_name = "scrape/index.html"
  form_class = RequestForm

  def form_valid(self, form):
    form.save()
    url = form.cleaned_data["url"]
    context = {
      "url": url,
      "form": self.form_class,
      "name": f"scrapoo {datetime.today()}"
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
