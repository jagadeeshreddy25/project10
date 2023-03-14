from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':200,'b':40}
    return render(request,'conditions.html',d)
def loop(request):
    d={'name':'jaggu'}
    return render(request,'loop.html',d)

