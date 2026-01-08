from django.shortcuts import render

# Create your views here.

def home(request):
  pt = "piks/html/home.html"
  dt = {
    "nm":"Vishal Gaud",
  }
  return render(request, pt, dt)