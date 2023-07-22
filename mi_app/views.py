from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request, "mi_app/index.html", {})