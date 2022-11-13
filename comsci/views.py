from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homepage(request):
    pic = {
        'item':['csp2.jpg', 'csp3.jpg', 'csp4.jpg', 'csp5.jpg']
    }
    return render(request, 'home.html', pic)

def students(request):
    return render(request, 'index.html')